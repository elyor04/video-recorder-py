## To install required libraries

### Update your system and install pip
```
sudo apt update && sudo apt -y upgrade && sudo apt -y install python3-pip
```

### To Get a Better Performance install Intel GPU driver and libraries
* NOTE: it works well with Linux Ubuntu 22.04.3 LTS 64-bit
* WARNING: if you don't have Intel GPU, please skip this part
```
sudo apt -y install intel-opencl-icd opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo && clinfo -l
```

### Install the libraries
```
pip install --upgrade numpy opencv-python "PyQt6-sip<13.5" "PyQt6-Qt6<6.5" "PyQt6<6.5"
```
