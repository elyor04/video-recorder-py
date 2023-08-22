## To install required libraries

Open your terminal and go to home directory
```
cd ~
```

Update your system
```
sudo apt-get update && sudo apt-get -y upgrade
```

Install intel gpu driver and library (WARNING: if you don't have intel gpu, please skip this part)
```
sudo apt-get -y install intel-opencl-icd ocl-icd-opencl-dev clinfo && clinfo -l
```

Install dependencies
```
sudo apt-get -y install build-essential cmake git pkg-config libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libopenexr-dev libjasper-dev libv4l-dev libxvidcore-dev libx264-dev libatlas-base-dev gfortran python3-dev python3-pip
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
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_OPENCL=ON -D WITH_FFMPEG=ON -D WITH_FAST_MATH=ON -D WITH_QT=ON -D BUILD_opencv_python3=ON -D BUILD_opencv_python2=OFF -D PYTHON_DEFAULT_EXECUTABLE=$(which python3) ..
```

Build and install OpenCV
```
make -j$(nproc) && sudo make install
```

Verify OpenCV Installation
```
python3 -c "import cv2; print(cv2.__version__)"
```

Install PyQt6 library
```
pip3 install --upgrade PyQt6-sip==13.4.1 PyQt6-Qt6==6.4.2 PyQt6==6.4.2
```
