# GUIRobotCovid
Implementasi GUI PyQt5 dan RosTopic

## Installation Libraries

Install PyQt5 and QtDesigner, it should work on Python 2.7 or 3.x series

```bash
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
```
## Running QtDesigner
if you want to re-design using Qt Designer, please do this following configuration steps:
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


