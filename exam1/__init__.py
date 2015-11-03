
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Model



class Exam1(QMainWindow):
  
  def __init__(self, parent=None):
        super(Exam1, self).__init__()
        
        self.setWindowTitle("Exam1 template")
        self.initUI()

  
  def initUI(self):
      
  def run(self):
        self.show()
        sys.exit(app.exec_())
      
      
      
app = QApplication(sys.argv):
Exam1().run()
