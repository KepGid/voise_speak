import pyaudio
import wave

import threading
import keyboard
from threading import Thread,activeCount
import pyaudio
from PyQt5 import QtCore, QtWidgets, QtGui, uic, QtMultimedia
import sys
import time


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.slovar_the_key_qt = {'1': 49, '2': 50, '3': 51, '4': 52, '5': 53,
                               '6': 54, '7': 55, '8': 56, '9': 57, '0': 48,
                               '-': 45, '=': 61,'q': 81, 'w': 87, 'e': 69,
                               'r': 82, 't': 84, 'y': 89, 'u': 85, 'i': 73,
                               'o': 79, 'p': 80, '[': 91, ']': 93,'a': 65,
                               's': 83, 'd': 68, 'f': 70, 'g': 71, 'h': 72,
                               'j': 74, 'k': 75, 'l': 76, ';': 59, "'": 39,
                               '\\': 92,'z': 90, 'x': 88, 'c': 67, 'v': 86,
                               'b': 66, 'n': 78, 'm': 77, ',': 44, '.': 46, '/': 47}
        self.slovar_the_key_qt = {'1': 30, '2': 30, '3': 30, '4': 30, '5': 30,
                               '6': 30, '7': 30, '8': 30, '9': 30, '0': 30,
                               '-': 30, '=': 30, 'q': 30, 'w': 30, 'e': 30,
                               'r': 30, 't': 30, 'y': 30, 'u': 30, 'i': 30,
                               'o': 30, 'p': 30, '[': 30, ']': 30, 'a': 30,
                               's': 30, 'd': 30, 'f': 30, 'g': 30, 'h': 30,
                               'j': 30, 'k': 30, 'l': 30, ';': 30, "'": 30,
                               '\\': 30,'z': 30, 'x': 30, 'c': 30, 'v': 30,
                               'b': 30, 'n': 30, 'm': 30, ',': 30, '.': 30, '/': 30}

        self.slovar_the_key ={ 41: '`', 2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6',
                               8: '7', 9: '8', 10: '9', 11: '0', 12: '-', 13: '=',
                               14: 'backspace', 15: 'tab', 16: 'Q', 17: 'W', 18: 'E',
                               19: 'R', 20: 'T', 21: 'Y', 22: 'U', 23: 'I', 24: 'O',
                               25: 'P', 26: '[', 27: ']', 28: 'enter', 58: 'caps lock',
                               30: 'a', 31: 's', 32: 'd', 33: 'f', 34: 'g', 35: 'h',
                               36: 'j', 37: 'k', 38: 'l', 39: ';', 40: "'", 43: '\\',
                               42: 'shift', 44: 'z', 45: 'x', 46: 'c', 47: 'v', 48: 'b',
                               49: 'n', 50: 'm', 51: ',', 52: '.', 53: '/', 54: 'right shift'}

        self.key_for_audio = {}


        line_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', ]
        line_2 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', ]
        line_3 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\\', ]
        line_4 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', ]

        self.vbox = QtWidgets.QVBoxLayout()

        self.vbox_for_key = QtWidgets.QVBoxLayout()

        hbox_1 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton('`')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(30, 30)
        hbox_1.addWidget(self.button)

        self.add_key_in_layout(hbox_1, line_1, 0)

        self.button = QtWidgets.QPushButton('backspace')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(70, 30)
        hbox_1.addWidget(self.button)
        hbox_1.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))
        #-------------------------------------------
        hbox_2 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton('tab')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(50, 30)
        hbox_2.addWidget(self.button)

        self.add_key_in_layout(hbox_2, line_2, 0)

        self.button = QtWidgets.QPushButton('enter')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(50, 30)
        hbox_2.addWidget(self.button)
        hbox_2.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))
        #-------------------------------------------
        hbox_3 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton('caps lock')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(60, 30)
        hbox_3.addWidget(self.button)

        self.add_key_in_layout(hbox_3, line_3, 0)

        self.button = QtWidgets.QPushButton('enter')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(40, 30)
        hbox_3.addWidget(self.button)
        hbox_3.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))
        #-------------------------------------------
        hbox_4 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton('shift')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(70, 30)
        hbox_4.addWidget(self.button)

        self.add_key_in_layout(hbox_4, line_4, 0)

        self.button = QtWidgets.QPushButton('righ shift')
        self.button.clicked.connect(self.test)
        self.button.setFixedSize(102, 30)
        hbox_4.addWidget(self.button)
        hbox_4.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))
        #-------------------------------------------
        btn = QtWidgets.QPushButton("new")
        btn.setStyleSheet("background-color: #00ff00")

        #self.setMask(window_forma.mask())



        hbox_btn = QtWidgets.QHBoxLayout()
        hbox_btn.addWidget(btn)
        hbox_btn.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        self.vbox_for_key.addLayout(hbox_1)
        self.vbox_for_key.addLayout(hbox_2)
        self.vbox_for_key.addLayout(hbox_3)
        self.vbox_for_key.addLayout(hbox_4)
        self.vbox_for_key.addLayout(hbox_btn)
        self.vbox.addLayout(self.vbox_for_key)

        # self.vbox.addSpacing(340)
        # vbox.addItem(QtWidgets.QSpacerItem(0,10,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))

        # ----------- customization window ---------------

        self.setLayout(self.vbox)

        #self.setWindowOpacity(0.8)
        self.resize(800, 540)
        #self.resize(540, 540)

        self.stop = False
        self.new_click = False

    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            # self.new_click = not self.new_click
            if self.new_click == True:
                self.stop = True
            else:
                self.stop = False
            self.voise_play(e.key())

            print("cod - ", e.key(), " text - ", e.text())

        return QtWidgets.QWidget.event(self, e)



    def add_key_in_layout(self, layout, array_key, spasing):
        if spasing != 0:
            layout.addSpacing(spasing)

        for i in range(len(array_key)):
            self.button = QtWidgets.QPushButton(array_key[i])
            self.button.clicked.connect(self.test)
            self.button.setFixedSize(30, 30)
            layout.addWidget(self.button)
        #layout.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))

    def test(self):
        name_button = self.sender()
        #file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self,
        #                                            caption="choose audio file",
        #                                            filter="Audio file (*.wav)")
        file_name = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                    caption="choose audio file",
                                                    filter="Audio file (*.wav)")
        if file_name[0] == '':
            return
        print(file_name)

        cod = self.slovar_the_key.get(name_button.text())
        self.key_for_audio[cod] = file_name[0]
        name_button.setStyleSheet("background-color: #00ff00")




       # print(name_button.text())

    def test_1(self):
        print('NEWWWW')

    def voise_play(self,cod_key):

       # print(cod_key)

        if self.key_for_audio.get(cod_key,0) == 0:
            return
        name_file  = self.key_for_audio.get(cod_key)
        #self.play_word(name_file)
        print('new potock')
        thread = Thread(target= self.play_word, args=(name_file,),name = 'main_thread')
        thread.start()




    def play_word(self,name):
        self.new_click = True


        print(activeCount())
        CHUNK = 1024
        wf = wave.open(name, 'rb')
        p = pyaudio.PyAudio()

        index_device = 6

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        input_device_index=None)
                        #output_device_index=index_device)

        data = wf.readframes(CHUNK)
        print("Start")

        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)
            #print(activeCount())
            count_p = activeCount()
            print(count_p)
            if self.stop == True and count_p >= 3: # bad very bad release
                #self.new_click = False
                print('STOP')
                return

        print(' --  ',activeCount())

        print("END")
        self.new_click = False

        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("player")

    # icon = QtGui.QIcon('image/close.png')
    # window.setWindowIcon(icon)
    # app.setWindowIcon(icon)
    # window.resize(400,600)
    window.show()
    sys.exit(app.exec_())

