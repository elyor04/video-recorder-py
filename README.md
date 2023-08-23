# hikvision-ip-camera-video-recorder (python)
* works for linux 64-bit and windows 64-bit
* may work for linux 32-bit and windows 32-bit


<div align="center">
<h3>How does the program look like?</h3><br>
<a target="_blank" href="https://imageupload.io/D84WNVQvHhvGOWg"><img src="https://imageupload.io/ib/2C8KQqXqwpfOBvI_1692765002.png" alt="Tab-1"/></a><br>
<a target="_blank" href="https://imageupload.io/hfiiKypQbnwSK3G"><img src="https://imageupload.io/ib/3Gmcv7Tk6x48vJn_1692765002.png" alt="Tab-2"/></a><br>
<a target="_blank" href="https://imageupload.io/VuvH19mjbQ0ZF1B"><img src="https://imageupload.io/ib/sozOPAsTzvKtMot_1692765002.png" alt="Tab-3"/></a><br>
</div>


## To install required libraries on linux

### Update your system and install pip
```
sudo apt update && sudo apt -y upgrade && sudo apt -y install python3-pip
```

### To get a better performance install Intel GPU driver and libraries
* NOTE: it works well with Linux Ubuntu 22.04.3 LTS 64-bit
* WARNING: if you don't have Intel GPU, please skip this part
```
sudo apt -y install intel-opencl-icd opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo && clinfo -l
```

### Install the libraries
```
pip install --upgrade numpy opencv-python "PyQt6-sip<13.5" "PyQt6-Qt6<6.5" "PyQt6<6.5"
```


## To install required libraries on windows

### Install the libraries
```
pip install --upgrade numpy opencv-python PyQt6
```
