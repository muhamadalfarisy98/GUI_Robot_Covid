# GUIRobotCovid
Implementasi GUI PyQt5 dan RosTopic

## Installation

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
##Code Generation

```bash
pyuic5 -x your_file.ui -o your_python_file.py
```
## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

##Name
Self name explaining

##Description
a list of feature
##Project status
#authors and acknowledgement
