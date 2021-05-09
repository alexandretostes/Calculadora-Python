import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   e4 = QLineEdit(widget)
   e3 = QLineEdit(widget)
   e4.move(64,100)
   e3.move(64, 120)
   def clique_botao():
      resp = int(e4.text()) + int(e3.text())
      textLabel.setText (str(resp))

   def clique_Sub():
      resp = int(e4.text()) - int(e3.text())
      textLabel.setText (str(resp))

   button1 = QPushButton(widget)
   button1.setText("Botão 1")
   button1.move(64, 32)
   button1.clicked.connect(clique_botao)

   button2 = QPushButton(widget)
   button2.setText("Botão 2")
   button2.move(160, 32)
   button2.clicked.connect(clique_Sub)

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!")
   textLabel.move(110,85)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()