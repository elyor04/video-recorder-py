BASE_DIR=$(dirname "$(readlink -f "$0")")

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$BASE_DIR/HKIPcamera/lib"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$BASE_DIR/HKIPcamera/lib/HCNetSDKCom"

python3 "$BASE_DIR/main.py" "$@"
