from ctypes import (
    Structure,
    c_ubyte,
    c_ushort,
    c_int,
    c_uint,
)
from cv2 import UMat
from platform import system, architecture
from os.path import join, dirname
from re import findall
from typing import Any


def get_platform_info():
    sys_platform = system().lower().strip()
    python_bit = architecture()[0]
    python_bit_num = findall("(\d+)\w*", python_bit)[0]
    return sys_platform, python_bit_num


sys_platform, python_bit_num = get_platform_info()
system_type = sys_platform + python_bit_num

if sys_platform == "linux":
    from ctypes import cdll, CFUNCTYPE

    loadLibrary = cdll.LoadLibrary
    FUNCTYPE = CFUNCTYPE
elif sys_platform == "windows":
    from ctypes import windll, WINFUNCTYPE

    loadLibrary = windll.LoadLibrary
    FUNCTYPE = WINFUNCTYPE
else:
    print("Hikvision Net SDK does not support this platform")
    exit(0)

libsDir = join(dirname(__file__), "libs")

netSdkPath_dict = {
    "windows64": join(libsDir, "win64", "HCNetSDK.dll"),
    "windows32": join(libsDir, "win32", "HCNetSDK.dll"),
    "linux64": join(libsDir, "linux64", "libhcnetsdk.so"),
    "linux32": join(libsDir, "linux32", "libhcnetsdk.so"),
}
playSdkPath_dict = {
    "windows64": join(libsDir, "win64", "PlayCtrl.dll"),
    "windows32": join(libsDir, "win32", "PlayCtrl.dll"),
    "linux64": join(libsDir, "linux64", "libPlayCtrl.so"),
    "linux32": join(libsDir, "linux32", "libPlayCtrl.so"),
}

netSdkPath = netSdkPath_dict[system_type]
playSdkPath = playSdkPath_dict[system_type]

BYTE = c_ubyte
WORD = c_ushort
LONG = c_int
DWORD = c_uint
HWND = c_uint

NULL = 0
EXCEPTION_RECONNECT = 0x8005
NET_DVR_SYSHEAD = 1
NET_DVR_STREAMDATA = 2
T_YV12 = 3


class NET_DVR_DEVICEINFO_V30(Structure):
    _fields_ = [
        ("sSerialNumber", BYTE * 48),
        ("byAlarmInPortNum", BYTE),
        ("byAlarmOutPortNum", BYTE),
        ("byDiskNum", BYTE),
        ("byDVRType", BYTE),
        ("byChanNum", BYTE),
        ("byStartChan", BYTE),
        ("byAudioChanNum", BYTE),
        ("byIPChanNum", BYTE),
        ("byZeroChanNum", BYTE),
        ("byMainProto", BYTE),
        ("bySubProto", BYTE),
        ("bySupport", BYTE),
        ("bySupport1", BYTE),
        ("bySupport2", BYTE),
        ("wDevType", WORD),
        ("bySupport3", BYTE),
        ("byMultiStreamProto", BYTE),
        ("byStartDChan", BYTE),
        ("byStartDTalkChan", BYTE),
        ("byHighDChanNum", BYTE),
        ("bySupport4", BYTE),
        ("byLanguageType", BYTE),
        ("byVoiceInChanNum", BYTE),
        ("byStartVoiceInChanNo", BYTE),
        ("bySupport5", BYTE),
        ("bySupport6", BYTE),
        ("byMirrorChanNum", BYTE),
        ("wStartMirrorChanNo", WORD),
        ("bySupport7", BYTE),
        ("byRes2", BYTE),
    ]


class NET_DVR_PREVIEWINFO(Structure):
    _fields_ = [
        ("lChannel", LONG),
        ("dwStreamType", DWORD),
        ("dwLinkMode", DWORD),
        ("hPlayWnd", HWND),
        ("bBlocked", DWORD),
        ("bPassbackRecord", DWORD),
        ("byPreviewMode", BYTE),
        ("byStreamID", BYTE * 32),
        ("byProtoType", BYTE),
        ("byRes1", BYTE),
        ("byVideoCodingType", BYTE),
        ("dwDisplayBufNum", DWORD),
        ("byNPQMode", BYTE),
        ("byRecvMetaData", BYTE),
        ("byDataType", BYTE),
        ("byRes", BYTE * 213),
    ]


class FRAME_INFO(Structure):
    _fields_ = [
        ("nWidth", LONG),
        ("nHeight", LONG),
        ("nStamp", LONG),
        ("nType", LONG),
        ("nFrameRate", LONG),
        ("dwFrameNum", DWORD),
    ]


def _func(bgrUMat: UMat, pUser: Any) -> None:
    pass


IMAGEDATACALLBACK = type(_func)
