from .sdk_struct import loadLibrary, netSdkPath, NET_DVR_DEVICEINFO, NET_DVR_CLIENTINFO
from ctypes import byref


class HKIPcamera:
    def __init__(self) -> None:
        self.netSdk = loadLibrary(netSdkPath)
        self.userId = -1
        self.realPlayHandle = -1
        self.init()

    def init(self) -> bool:
        return bool(self.netSdk.NET_DVR_Init())

    def cleanup(self) -> bool:
        return bool(self.netSdk.NET_DVR_Cleanup())

    def login(self, ip: str, usr: str, password: str, port: int = 8000) -> bool:
        deviceInfo = NET_DVR_DEVICEINFO()

        self.userId = self.netSdk.NET_DVR_Login(
            ip.encode(), port, usr.encode(), password.encode(), byref(deviceInfo)
        )
        return self.userId >= 0

    def logout(self) -> bool:
        return bool(self.netSdk.NET_DVR_Logout(self.userId))

    def realPlay(self, playWnd: int = 0, channel: int = 1, linkMode: int = 0) -> bool:
        clientInfo = NET_DVR_CLIENTINFO()
        clientInfo.hPlayWnd = playWnd
        clientInfo.lChannel = channel
        clientInfo.lLinkMode = linkMode

        self.realPlayHandle = self.netSdk.NET_DVR_RealPlay(
            self.userId, byref(clientInfo)
        )
        return self.realPlayHandle >= 0

    def stopRealPlay(self) -> bool:
        return bool(self.netSdk.NET_DVR_StopRealPlay(self.realPlayHandle))

    def saveRealData(self, fileName: str) -> bool:
        return bool(
            self.netSdk.NET_DVR_SaveRealData(self.realPlayHandle, fileName.encode())
        )

    def stopSaveRealData(self) -> bool:
        return bool(self.netSdk.NET_DVR_StopSaveRealData(self.realPlayHandle))

    def release(self) -> None:
        self.stopSaveRealData()
        self.stopRealPlay()
        self.logout()
        self.cleanup()


if __name__ == "__main__":
    hkipc = HKIPcamera()
    success = hkipc.login("ip_address", "user_name", "password", 8000)
    if success:
        print("Connected successfully")
    else:
        print("Could not connect")
    hkipc.release()
