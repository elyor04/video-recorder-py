# hikvision-ip-camera-video-recorder (python)
* ### works on linux 64-bit and windows 64-bit
* ### may work on linux 32-bit and windows 32-bit


<div align="center">
<h2>How does the program look like?</h2>
<a href="https://ibb.co/XyMTGQ3"><img src="https://i.ibb.co/PT08VL9/Screenshot-from-2023-08-30-21-28-39.png" alt="Tab-1" border="0"></a><br>
<a href="https://ibb.co/3mF6RNw"><img src="https://i.ibb.co/7tpMkWH/Screenshot-from-2023-08-30-21-28-46.png" alt="Tab-2" border="0"></a><br>
<a href="https://ibb.co/c39ttsr"><img src="https://i.ibb.co/RbKPPJD/Screenshot-from-2023-08-30-21-32-44.png" alt="Tab-3" border="0"></a><br>
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
pip install opencv-python PyQt6
```


## Install on Windows

### Install required libraries
```
pip install --upgrade numpy opencv-python "PyQt6-sip<13.5" "PyQt6-Qt6<6.5" "PyQt6<6.5"
```
