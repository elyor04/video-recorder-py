from ctypes import Structure, c_ubyte, c_int, c_uint, c_char_p
from platform import system, architecture
from os.path import join, dirname
from re import findall


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
LONG = c_int
HWND = c_uint


class NET_DVR_DEVICEINFO(Structure):
    _fields_ = [
        ("sSerialNumber", BYTE * 48),
        ("byAlarmInPortNum", BYTE),
        ("byAlarmOutPortNum", BYTE),
        ("byDiskNum", BYTE),
        ("byDVRType", BYTE),
        ("byChanNum", BYTE),
        ("byStartChan", BYTE),
    ]


class NET_DVR_CLIENTINFO(Structure):
    _fields_ = [
        ("lChannel", LONG),
        ("lLinkMode", LONG),
        ("hPlayWnd", HWND),
        ("sMultiCastIP", c_char_p),
        ("byProtoType", BYTE),
        ("byRes", BYTE * 3),
    ]
