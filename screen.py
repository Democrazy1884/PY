from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

hwnd = win32gui.FindWindow(None, 'MI 9 SE')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")
