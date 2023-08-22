## To install required libraries

Open your terminal and go to home directory
```
cd ~
```

Update your system
```
sudo apt-get update && sudo apt-get -y upgrade
```

Install intel gpu driver and libraries (WARNING: if you don't have intel gpu, please skip this part)
```
sudo apt-get -y install intel-opencl-icd opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo && clinfo -l
```

Install dependencies
```
sudo apt-get -y install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python3-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libxvidcore-dev libx264-dev && sudo apt-get -y install ffmpeg python3-pip
```

Get OpenCV from the official repository
```
git clone https://github.com/opencv/opencv.git && cd opencv
```

Prepare for the build
```
mkdir build && cd build
```

Run cmake with OpenCL enabled
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_OPENCL=ON -D WITH_FFMPEG=ON -D ENABLE_FAST_MATH=1 -D WITH_QT=ON -D BUILD_opencv_python3=ON ..
```

Build and install OpenCV
```
make -j$(nproc) && sudo make install && cd ~
```

Verify OpenCV Installation
```
python3 -c "import cv2; print(cv2.__version__)"
```

Install PyQt6 library
```
pip3 install --upgrade PyQt6-sip==13.4.1 PyQt6-Qt6==6.4.2 PyQt6==6.4.2
```
