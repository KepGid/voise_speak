import sys
from PyQt5 import QtCore, QtWidgets, QtGui, uic, QtMultimedia

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.file = open('name_file.txt', 'w')# !!!!!!!!!!!!!

        self.resize(300, 300)


    def event(self,e):
        if e.type() == QtCore.QEvent.KeyPress:

            stroka = str("'"+str(e.text())+"': "+str(e.key())+", ")
            self.file.write(stroka)
            print("cod - ", e.key(), " text - ", e.text())
        return QtWidgets.QWidget.event(self, e)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())