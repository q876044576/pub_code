pyqt5 windows环境配置说明

1 安装python3.7到路径D:\Program Files\
到官网（https://www.python.org/）下载对应版本安装包，配置到系统变量Path
D:\Program Files\Python37
D:\Program Files\Python37\Scripts

2 pip安装pyqt5
执行命令
pip3 install pyqt5
pip3 install pyqt5-tools
pip3 install opencv-python
pip3 install pyinstaller

pip list 查看安装情况
Package          Version
---------------- ----------
click            7.1.2
numpy            1.21.6
opencv-python    4.5.5.64
pip              22.1.2
PyQt5            5.15.4
pyqt5-plugins    5.15.4.2.2
PyQt5-Qt5        5.15.2
PyQt5-sip        12.10.1
pyqt5-tools      5.15.4.3.2
python-dotenv    0.20.0
qt5-applications 5.15.2.2.2
qt5-tools        5.15.2.1.2
setuptools       47.1.0
---------------- ----------


3 配置VSCODE
安装扩展PYQT Integration
打开配置文件
配置项
Pyqt-integration › Linguist: Cmd
'linguist' command file, you can also specify a path
填写
D:\Program Files\Python37\Lib\site-packages\qt5_applications\Qt\bin\linguist.exe

配置项
Pyqt-integration › Pylupdate: Cmd
'pylupdate' command file, you can also specify a path
填写
D:\Program Files\Python37\Scripts\pylupdate5.exe

配置项
Pyqt-integration › Pyrcc: Cmd
'pyrcc' command file, you can also specify a path
填写
D:\Program Files\Python37\Scripts\pyrcc5.exe

配置项
Pyqt-integration › Pyuic: Cmd
'pyuic' command file, you can also specify a path
填写
D:\Program Files\Python37\Scripts\pyuic5.exe

配置项
Pyqt-integration › Qtdesigner: Path
Path of QT designer
填写
D:\Program Files\Python37\Lib\site-packages\qt5_applications\Qt\bin\designer.exe

编译可执行文件
pyinstaller -w -F main.py