from ctypes import (
    c_char,
    c_int,
    c_void_p,
    py_object,
    byref,
    POINTER,
    pointer,
    cast,
)
from .sdk_struct import (
    NET_DVR_DEVICEINFO_V30,
    NET_DVR_PREVIEWINFO,
    FRAME_INFO,
    LONG,
    DWORD,
    BYTE,
    NULL,
    T_YV12,
    NET_DVR_SYSHEAD,
    NET_DVR_STREAMDATA,
    EXCEPTION_RECONNECT,
    IMAGEDATACALLBACK,
    FUNCTYPE,
    loadLibrary,
    netSdkPath,
    playSdkPath,
)
from cv2 import ocl, UMat, cvtColor, COLOR_YUV2BGR_YV12
from time import time, sleep
from numpy import frombuffer, uint8
from typing import Any

_hkipc: "HKIPcamera" = None


def yv12toBGRMat(inYv12: POINTER(c_char), width: c_int, height: c_int) -> UMat:
    yuvHeight = int(height * 3 / 2)
    bufLen = int(width * yuvHeight)
    yv12Bytes = bytes(cast(inYv12, POINTER(c_char * bufLen)).contents)
    yv12Array = frombuffer(yv12Bytes, dtype=uint8)
    yv12Array = yv12Array.reshape((yuvHeight, width))
    return cvtColor(UMat(yv12Array), COLOR_YUV2BGR_YV12)


@FUNCTYPE(None, c_int, POINTER(c_char), c_int, POINTER(FRAME_INFO), c_void_p, c_int)
def DecCBFun(
    nPort: c_int,
    pBuf: POINTER(c_char),
    nSize: c_int,
    pFrameInfo: POINTER(FRAME_INFO),
    pUser: c_void_p,
    nReserved2: c_int,
) -> None:
    frameInfo = cast(pFrameInfo, POINTER(FRAME_INFO)).contents

    if _hkipc.fImageDataCallBack_ is None:
        return
    if frameInfo.nType == T_YV12:
        bgrUMat = yv12toBGRMat(pBuf, frameInfo.nWidth, frameInfo.nHeight)
        _hkipc.fImageDataCallBack_(bgrUMat, _hkipc.pUser_)


@FUNCTYPE(None, LONG, DWORD, POINTER(BYTE), DWORD, c_void_p)
def fRealDataCallBack(
    lRealHandle: LONG,
    dwDataType: DWORD,
    pBuffer: POINTER(BYTE),
    dwBufSize: DWORD,
    pUser: c_void_p,
) -> None:
    if lRealHandle != _hkipc.lRealPlayHandle_:
        return

    if dwDataType == NET_DVR_SYSHEAD:
        if not _hkipc.playSdk.PlayM4_GetPort(byref(_hkipc.nPort_)):
            return
        if dwBufSize > 0:
            if not _hkipc.playSdk.PlayM4_OpenStream(
                _hkipc.nPort_, pBuffer, dwBufSize, 1024 * 1024
            ):
                return
            if not _hkipc.playSdk.PlayM4_SetDecCallBackMend(
                _hkipc.nPort_, DecCBFun, c_void_p(pUser)
            ):
                return
            if not _hkipc.playSdk.PlayM4_Play(_hkipc.nPort_, NULL):
                return

    elif dwDataType == NET_DVR_STREAMDATA:
        if (dwBufSize > 0) and (_hkipc.nPort_ != -1):
            inData = _hkipc.playSdk.PlayM4_InputData(_hkipc.nPort_, pBuffer, dwBufSize)
            while not inData:
                print("PlayM4_InputData failed")
                sleep(10)
                inData = _hkipc.playSdk.PlayM4_InputData(
                    _hkipc.nPort_, pBuffer, dwBufSize
                )


@FUNCTYPE(None, DWORD, LONG, LONG, c_void_p)
def g_ExceptionCallBack(
    dwType: DWORD, user_id_: LONG, lHandle: LONG, pUser: c_void_p
) -> None:
    if dwType == EXCEPTION_RECONNECT:
        print("----------reconnect--------", time())
    else:
        print("Exception:", dwType)


class HKIPcamera:
    def __init__(self) -> None:
        global _hkipc
        self.netSdk = loadLibrary(netSdkPath)
        self.playSdk = loadLibrary(playSdkPath)

        self.user_id_ = -1
        self.lRealPlayHandle_ = -1
        self.nPort_ = LONG(-1)
        self.channel_ = 1
        self.streamtype_ = 0
        self.linkmode_ = 0
        self.struDeviceInfo_ = NET_DVR_DEVICEINFO_V30()
        self.fImageDataCallBack_ = None
        self.pUser_ = None

        ocl.setUseOpenCL(True)
        _hkipc = self

    def login(
        self,
        ip: str,
        usr: str,
        password: str,
        port: int = 8000,
        channel: int = 1,
        streamtype: int = 0,
        linkmode: int = 0,
    ) -> bool:
        self.netSdk.NET_DVR_Init()
        self.netSdk.NET_DVR_SetConnectTime(2000, 1)
        self.netSdk.NET_DVR_SetReconnect(10000, 1)
        if not self._openCamera(ip, usr, password, port):
            self.netSdk.NET_DVR_Cleanup()
            return False
        self.channel_ = channel
        self.streamtype_ = streamtype
        self.linkmode_ = linkmode
        if not self._readCamera():
            self.netSdk.NET_DVR_Logout(self.user_id_)
            self.netSdk.NET_DVR_Cleanup()
            return False
        return True

    def _openCamera(self, ip: str, usr: str, password: str, port: int = 8000) -> bool:
        self.user_id_ = self.netSdk.NET_DVR_Login_V30(
            ip.encode(),
            port,
            usr.encode(),
            password.encode(),
            byref(self.struDeviceInfo_),
        )
        if self.user_id_ < 0:
            print(
                "Login failed! Error number:",
                self.netSdk.NET_DVR_GetLastError(),
            )
            return False
        return True

    def _readCamera(self) -> bool:
        self.netSdk.NET_DVR_SetExceptionCallBack_V30(0, NULL, g_ExceptionCallBack, NULL)

        previewInfo = NET_DVR_PREVIEWINFO()
        previewInfo.hPlayWnd = NULL
        previewInfo.lChannel = int(self.struDeviceInfo_.byStartDChan) + self.channel_
        previewInfo.dwStreamType = self.streamtype_
        previewInfo.dwLinkMode = self.linkmode_

        self.lRealPlayHandle_ = self.netSdk.NET_DVR_RealPlay_V40(
            self.user_id_, byref(previewInfo), fRealDataCallBack, NULL
        )
        if self.lRealPlayHandle_ < 0:
            print(
                "NET_DVR_RealPlay_V30 failed! Error number:",
                self.netSdk.NET_DVR_GetLastError(),
            )
            return False
        return True

    def setImageDataCallBack(
        self, fImageDataCallBack: IMAGEDATACALLBACK, pUser: Any = None
    ) -> None:
        self.fImageDataCallBack_ = fImageDataCallBack
        self.pUser_ = pUser

    def release(self) -> None:
        self.netSdk.NET_DVR_StopRealPlay(self.lRealPlayHandle_)
        self.netSdk.NET_DVR_Logout(self.user_id_)
        self.netSdk.NET_DVR_Cleanup()


if __name__ == "__main__":
    hkipc = HKIPcamera()
    success = hkipc.login("ip_address", "user_name", "password", 8000)
    if success:
        print("Connected successfully")
    else:
        print("Could not connect")
    hkipc.release()
