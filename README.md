# GUIRobotCovid
Implementasi GUI PyQt5 dan RosTopic

# Description
this project is used for **Human and Robot interaction, controlling action, Input data system, and support robot conditioning**.

## Installation Libraries

Install PyQt5 and QtDesigner, it should work on *Python 2.7 or 3.x series*

```bash
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
```
## Running QtDesigner
if you want to re-design using Qt Designer, 
> please do this following configuration steps:
```bash
cd /usr/lib/x86_64-linux-gnu/qt5/bin/
./designer
```
## Code Generation

```bash
pyuic5 -x your_file.ui -o your_python_file.py
```
## How To Use ?
1. go to LoginFile folder
2. Run `robotgui.py`
after that running

3. go to RemoteUi folder
4. run `remotegui.py`

## Reference
[Qt Python](https://pythonbasics.org/qt-designer-python/)

## Install ROS
Installation of ROS

[ROS WIKI](http://wiki.ros.org/melodic/Installation/Ubuntu)

## TurtleBot
```bash
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup
```
## OpenCR Setup
```bash
https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/
```
## SETUP ROS
```bash
awal2:
1. mkdir catkin_ws
2. mkdir src
3. cd.. && catkin_make
4. clone repos
```

## CMD SETUP
```bash
ROS
source /opt/ros/noetic/setup.zsh
source /home/faris/Documents/catkin_ws/devel/setup.zsh
alias cm="/home/faris/Documents/catkin_ws && catkin_make"
alias eb='nano ~/.zshrc'
alias sb='source ~/.zshrc'

export TURTLEBOT3_MODEL=covid

connection
export ROS_MASTER_URI=localhost
export ROS_HOSTNAME=localhost`
```
