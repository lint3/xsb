from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog, QGraphicsView,
                             QGraphicsScene, QHBoxLayout, QVBoxLayout, QGridLayout,
                             QGraphicsPixmapItem)
from PyQt5.QtGui import QPixmap
import sys
from xstitch import *

    
class App(QWidget):
  
  def __init__(self):
    super().__init__()
    self.timesRendered = 0
    self.setup_ui()
  
  
  def render(self):
    self.timesRendered += 1
    print("Rendered " + str(self.timesRendered) + " times.")
  
  
  def open(self):
    self.path, _ = QFileDialog.getOpenFileName(self, "Pick Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp")
    if self.path:
      print("File opened.")
      scene = QGraphicsScene(self)
      pixmap = QPixmap(self.path)
      pixItem = QGraphicsPixmapItem(pixmap)
      self.s1.addItem(pixItem)
      self.render()
  
  
  def setup_ui(self):
    controls = QWidget()
    controlsStack = QVBoxLayout()
    controls.setLayout(controlsStack)
    
    LoadFileButton = QPushButton('Load Image')
    LoadFileButton.clicked.connect(self.open)
    
    RenderButton = QPushButton('Render')
    RenderButton.clicked.connect(self.render)
    
    MyButton = QPushButton('Dejigamaflip')
    
    
    for item in [LoadFileButton, RenderButton, MyButton]:
      controlsStack.addWidget(item)
    
    
    preview = QWidget()
    previewStack = QVBoxLayout()
    preview.setLayout(previewStack)
    
    testbutton = QPushButton("Test Button")
    
    self.s1 = QGraphicsScene()
    self.s1.addText("Test1")
    self.s2 = QGraphicsScene()
    self.s2.addText("Test2")
    self.s3 = QGraphicsScene()
    self.s3.addText("Test3")
    
    self.inputImage = QGraphicsView(self.s1)
    self.processedImage = QGraphicsView(self.s2)
    self.outputImage = QGraphicsView(self.s3)
    
    for item in [self.inputImage, self.processedImage, self.outputImage]:
      previewStack.addWidget(item)
    
    
    hsplit = QHBoxLayout()
    hsplit.addWidget(controls)
    hsplit.addWidget(preview)
    
    self.setLayout(hsplit)
    self.setGeometry(1200, 200, 600, 600)
    self.setWindowTitle('XSB')
    self.show()
  
  
if __name__=="__main__":
  app = QApplication(sys.argv)
  win = App()
  win.show()
  app.exec()
