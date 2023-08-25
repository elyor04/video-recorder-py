# hikvision-ip-camera-video-recorder (python)
* ### works on linux 64-bit and windows 64-bit
* ### may work on linux 32-bit and windows 32-bit


<div align="center">
<h2>How does the program look like?</h2>
<a target="_blank" href="https://imageupload.io/D84WNVQvHhvGOWg"><img src="https://imageupload.io/ib/2C8KQqXqwpfOBvI_1692765002.png" alt="Tab-1"/></a><br>
<a target="_blank" href="https://imageupload.io/hfiiKypQbnwSK3G"><img src="https://imageupload.io/ib/3Gmcv7Tk6x48vJn_1692765002.png" alt="Tab-2"/></a><br>
<a target="_blank" href="https://imageupload.io/VuvH19mjbQ0ZF1B"><img src="https://imageupload.io/ib/sozOPAsTzvKtMot_1692765002.png" alt="Tab-3"/></a><br>
</div>


## Install on Linux

### Update your system and install pip
```
sudo apt update && sudo apt -y upgrade && sudo apt -y install python3-pip
```

### To get a better performance install Intel GPU driver and libraries
* WARNING: if you don't have Intel GPU, please skip this part
* NOTE: it's working well with Linux Ubuntu 22.04.3 LTS 64-bit
```
sudo apt -y install intel-opencl-icd opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev
```

### Install required libraries
```
pip install --upgrade numpy opencv-python "PyQt6-sip<13.5" "PyQt6-Qt6<6.5" "PyQt6<6.5"
```


## Install on Windows

### Install required libraries
```
pip install --upgrade numpy opencv-python "PyQt6-sip<13.5" "PyQt6-Qt6<6.5" "PyQt6<6.5"
```
