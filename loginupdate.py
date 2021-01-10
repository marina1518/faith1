from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType


import sys
from os import path

Class,_=loadUiType(path.join(path.dirname(__file__),"faith.ui"))

class marina(QMainWindow,Class):
   def __init__(self,parent=None):
      super(marina,self).__init__(parent)
      QMainWindow.__init__(self)
      self.setupUi(self)
      self.Handle_Ui()

   def Handle_Ui(self) :
      self.setWindowTitle('LOGIN')   




def main():
   app=QApplication(sys.argv)
   window=marina()
   window.show()
   app.exec_()

if __name__ == '__main__':
     main()