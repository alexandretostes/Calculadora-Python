import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   e4 = QLineEdit(widget)
   e3 = QLineEdit(widget)
   e4.move(95,100)
   e3.move(95, 140)
   def clique_botao():
      resp = int(e4.text()) + int(e3.text())
      textLabel.setText (str(resp))

   def clique_Sub():
      resp = int(e4.text()) - int(e3.text())
      textLabel.setText (str(resp))

   def clique_mult():
      resp = int(e4.text()) * int(e3.text())
      textLabel.setText (str(resp))

   def clique_div():
      resp = int(e4.text()) / int(e3.text())
      textLabel.setText (str(resp))

   def clique_exp():
      resp = int(e4.text()) ** int(e3.text())
      textLabel.setText(str(resp))

   button1 = QPushButton(widget)
   button1.setText("Soma")
   button1.move(5, 10)
   button1.clicked.connect(clique_botao)

   button2 = QPushButton(widget)
   button2.setText("Subtração")
   button2.move(100, 10)
   button2.clicked.connect(clique_Sub)

   button3 = QPushButton(widget)
   button3.setText("Multiplicação")
   button3.move(195, 10)
   button3.clicked.connect(clique_mult)

   button4 = QPushButton(widget)
   button4.setText("Divisão")
   button4.move(40, 40)
   button4.clicked.connect(clique_div)

   button5 = QPushButton(widget)
   button5.setText("Expotencialização")
   button5.move(135, 40)
   button5.clicked.connect(clique_exp)

   textLabel = QLabel(widget)
   textLabel.setText("Faça seu Calculo!")
   textLabel.move(100,80)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()