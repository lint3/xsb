from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog, QGraphicsView,
                             QGraphicsScene, QHBoxLayout, QVBoxLayout, QGridLayout)
import sys
from xstitch import *

class ControlsUI(QWidget):
  def __init__(self, parentContext):
    super().__init__()
    self.context = parentContext
    self.UI()
    
  def open(self):
    self.path, _ = QFileDialog.getOpenFileName(self, "Pick Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp")
    if self.path:
      self.context.fileOpened()
    
  def UI(self):
    LoadFileButton = QPushButton('Load Image')
    LoadFileButton.clicked.connect(self.open)
    
    RenderButton = QPushButton('Render')
    RenderButton.clicked.connect(self.context.render)
    
    MyButton = QPushButton('Dejigamaflip')
    vstack = QVBoxLayout()
    
    for item in [LoadFileButton, RenderButton, MyButton]:
      vstack.addWidget(item)
      
    self.setLayout(vstack)
    

class PreviewUI(QWidget):
  def __init__(self, parentContext):
    super().__init__()
    self.context = parentContext
    self.UI()
    
  
  def UI(self):
    vstack = QVBoxLayout()
    testbutton = QPushButton("Test Button")
    
    s1 = QGraphicsScene()
    s1.addText("Test1")
    s2 = QGraphicsScene()
    s2.addText("Test2")
    s3 = QGraphicsScene()
    s3.addText("Test3")
    
    self.inputImage = QGraphicsView(s1)
    self.processedImage = QGraphicsView(s2)
    self.outputImage = QGraphicsView(s3)
    
    for item in [self.inputImage, self.processedImage, self.outputImage]:
      vstack.addWidget(item)
      
    self.setLayout(vstack)
  
class ParentUI(QWidget):
  def __init__(self, parentContext):
    super().__init__()
    self.context = parentContext
    self.UI()
    
  def UI(self):
    controls = ControlsUI(self.context)
    self.preview = PreviewUI(self.context)
    
    hsplit = QHBoxLayout()
    hsplit.addWidget(controls)
    hsplit.addWidget(self.preview)
    
    self.setLayout(hsplit)
    self.setGeometry(1200, 200, 600, 600)
    self.setWindowTitle('XSB')
    self.show()

class Context():
  def __init__(self):
    self.timesRendered = 0
  
  def render(self):
    self.timesRendered += 1
    print("Rendered " + str(self.timesRendered) + " times.")
  
  def fileOpened(self):
    print("File opened.")
    scene = QGraphicsScene(self.preview)
    pixmap = QPixmap(self.preview.filepath)
    pixItem = QGraphicsPixmapItem(pixmap)
    self.preview.inputImage.addItem(pixItem)
    self.render()


  
if __name__=="__main__":
  appContext = Context()
  app = QApplication(sys.argv)
  win = ParentUI(appContext)
  win.show()
  app.exec()
