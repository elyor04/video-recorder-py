#!/bin/sh

BASE_DIR=$(dirname "$(readlink -f "$0")")

platform=$(uname -s | grep -o "^[a-zA-Z0-9_]*")
arch=$(uname -m)

if [ "$platform" = "Linux" ]; then
    py=python3
    if [ "$arch" = "x86_64" ]; then
        echo "Linux 64-bit"
        export LD_LIBRARY_PATH="$BASE_DIR/HKIPcamera/libs/linux64:$LD_LIBRARY_PATH"
        export LD_LIBRARY_PATH="$BASE_DIR/HKIPcamera/libs/linux64/HCNetSDKCom:$LD_LIBRARY_PATH"
    else
        echo "Linux 32-bit"
        export LD_LIBRARY_PATH="$BASE_DIR/HKIPcamera/libs/linux32:$LD_LIBRARY_PATH"
        export LD_LIBRARY_PATH="$BASE_DIR/HKIPcamera/libs/linux32/HCNetSDKCom:$LD_LIBRARY_PATH"
    fi
elif [ "$platform" = "Windows" ] || [ "$platform" = "Windows_NT" ] || [ "$platform" = "MSYS_NT" ] \
|| [ "$platform" = "CYGWIN" ] || [ "$platform" = "MINGW64_NT" ] || [ "$platform" = "MINGW32_NT" ]; then
    py=python
    if [ "$arch" = "x86_64" ]; then
        echo "Windows 64-bit"
        export PATH="$BASE_DIR/HKIPcamera/libs/win64:$PATH"
        export PATH="$BASE_DIR/HKIPcamera/libs/win64/HCNetSDKCom:$PATH"
    else
        echo "Windows 32-bit"
        export PATH="$BASE_DIR/HKIPcamera/libs/win32:$PATH"
        export PATH="$BASE_DIR/HKIPcamera/libs/win32/HCNetSDKCom:$PATH"
    fi
else
    echo "Hikvision Net SDK does not support this platform"
    exit 0
fi

$py "$BASE_DIR/main.py" "$@"
