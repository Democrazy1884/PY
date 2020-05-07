from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
 
hwnd = win32gui.FindWindow(None, 'D:\program\scrcpy-win64-v1.13\scrcpy-noconsole.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")