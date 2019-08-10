#Installation and running of donkey car python code depends on some other software package which we called as dependencies.
sudo apt-get install build-essential python3 python3-dev python3-virtualenv python3-     numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git

#To support  open cv  operations optional open cv dependencies  is installed.
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev      libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test


# Before installing donkey car python code it is compulsory to set up virtual env. 'Virtual  environment' is a tool to create isolated Python environments. The basic problem being addressed is one of dependencies and versions, and indirectly permissions. It can be set up by the following commands.
python3 -m virtualenv -p python3 env --system-site-packagesecho "source env/bin/activate" >> ~/.bashrcsource ~/.bashrc


# As we have opted dependencies earlier we can proceed in python.To perform all further programming steps, change a directory.
    mkdir projects
    cd projects

 # An updated donkey car library  is available in github. Pip is the package installer for the python. As we are installing in raspberry we  mention pi beside install. Tensor flow is  a library developed to accelerate machine learning equipments.
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
pip install -e .[pi]
pip install tensorflow==1.13.1

# Tensor flow install can be validated by:
python -c "import tensorflow"
While installing we will get warnings given below,they are ignored.
/home/pi/env/lib/python3.5/importlib/_bootstrap.py:222: RuntimeWarning: compiletime version 3.4 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.5
return f(*args, **kwds)
/home/pi/env/lib/python3.5/importlib/_bootstrap.py:222: RuntimeWarning: builtins.type size changed, may indicate binary incompatibility. Expected 432, got 412


# Donkey car can capture pictures by the usage of open cv. As we have already installed optional open cv dependencies ,we are ready to install our open cv. No errors are the sign of complete installations of open cv.
        pip install opencv-python
        python -c "import cv2"

#Change to a directory you would like to use as the head of your projects:
       mkdir projects
       cd projects
#Get the latest donkey from Github.
       git clone https://github.com/autorope/donkeycar
       cd donkeycar
       git checkout master
#If this is not your first install, update Conda and remove old donkey:
        conda update -n base -c defaults conda
        conda env remove -n donkey
#Create the Python anaconda environment
        conda env create -f install\envs\windows.yml
        conda activate donkey
        pip install -e .[pc]
#Optionally Install Tensorflow GPU and If you have an NVidia card, you should update to the lastest drivers and install Cuda SDK. 
        conda install tensorflow-gpu==1.13.1
#Create your local working dir:
        donkey createcar --path ~/mycar
# After closing the Anaconda Prompt, when you open it again,to re-enable the mappings to donkey specific Python libraries,you will need to type:
        conda activate donkey 


 The steering angle sensor is a critical part of ESC system that measures the steering wheel position angle and rate of turn.
       ⦁	Firstly, turn on your car
       ⦁	See to what channel servo cable is plugged into the PCA board, It should be either a 1        or a 0.
        ⦁	Run donkey calibrate –channel
                     < Your _ steering channel >--bus=1
        ⦁	By entering 360 you can see the wheels on our car moves slightly. If not enter 400 or 300.
         ⦁	Then enter values +/-10 from your starting value to find the PWM setting that makes your car then all the way left and all the way right Remember these values
⦁	Enter these values in myconfig.py script as STEERING_RIGHT_PWM and STEERING_LEFT_PWM.
