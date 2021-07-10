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
        self.slovar_1 = ['`', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', '0', '-', '=', 'backspace',
                    'spase', 'insert', 'home', 'page up', 'spase',
                    'num lock', '/', '*', '-']

        self.slovar_2 = ['tab', 'q', 'w', 'e', 'r', 't', 'y',
                    'u', 'i', 'o', 'p', '[', ']', 'enter',
                    'spase', 'delete', 'end', 'page down', 'spase',
                    'home', 'up', 'page up', '+']

        self.slovar_3 = ['caps lock', 'a', 's', 'd', 'f', 'g',
                    'h', 'j', 'k', 'l', ';', "'", '\\', 'enter',
                    'spase', 'left', 'clear', 'right', '+']

        self.slovar_4 = ['shift', 'z', 'x', 'c', 'v', 'b', 'n',
                    'm', ',', '.', '/', 'right shift', 'spase',
                    'up', 'spase', 'end', 'down', 'page down', 'enter']

        self.slovar_5 = ['ctrl', 'left windows', 'alt', 'space',
                    'right alt', 'spase', 'right ctrl', 'spase', 'left',
                    'down', 'right', 'spase', 'insert', 'delete', 'enter']

        self.slovar_1_size = [30, 30, 30, 30, 30, 30, 30,
                         30, 30, 30, 30, 30, 30, 70,
                         20, 30, 30, 30, 20,
                         30, 30, 30, 30]

        self.slovar_2_size = [50, 30, 30, 30, 30, 30, 30,
                         30, 30, 30, 30, 30, 30, 50,
                         20, 30, 30, 30, 20,
                         30, 30, 30, 30]
        self.slovar_3_size = [60, 30, 30, 30, 30, 30,
                         30, 30, 30, 30, 30, 30, 30, 40,
                         148, 30, 30, 30, 30]
        self.slovar_4_size = [70, 30, 30, 30, 30, 30, 30,
                         30, 30, 30, 30, 102, 55,
                         30, 57, 30, 30, 30, 30]
        self.slovar_5_size = [40, 40, 40, 200,
                         30, 127, 30, 20, 30,
                         30, 30, 20, 67, 30, 30]

        self.index_device = 5
        self.key_for_audio = {}

        self.vbox = QtWidgets.QVBoxLayout()

        self.vbox_for_key = QtWidgets.QVBoxLayout()

        hbox_1 = QtWidgets.QHBoxLayout()
        self.add_key_in_layout(hbox_1, self.slovar_1,self.slovar_1_size, 0)

        #-------------------------------------------
        hbox_2 = QtWidgets.QHBoxLayout()
        self.add_key_in_layout(hbox_2, self.slovar_2, self.slovar_2_size, 0)

        #-------------------------------------------
        hbox_3 = QtWidgets.QHBoxLayout()
        self.add_key_in_layout(hbox_3, self.slovar_3, self.slovar_3_size, 0)

        #-------------------------------------------
        hbox_4 = QtWidgets.QHBoxLayout()
        self.add_key_in_layout(hbox_4, self.slovar_4, self.slovar_4_size, 0)

        hbox_5 = QtWidgets.QHBoxLayout()
        self.add_key_in_layout(hbox_5, self.slovar_5, self.slovar_5_size, 0)

        #-------------------------------------------
        combo = QtWidgets.QComboBox()
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            stroka = str(p.get_device_info_by_index(i)['name'])
            combo.addItem(stroka)
        combo.activated.connect(self.set_index_device)
        combo.setCurrentIndex(self.index_device)

        #btn.setStyleSheet("background-color: #00ff00")

        #self.setMask(window_forma.mask())

        self.label_exception = QtWidgets.QLabel()
        hbox_btn = QtWidgets.QHBoxLayout()
        hbox_btn.addWidget(combo)
        hbox_btn.addWidget(self.label_exception)
        hbox_btn.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        self.vbox_for_key.addLayout(hbox_1)
        self.vbox_for_key.addLayout(hbox_2)
        self.vbox_for_key.addLayout(hbox_3)
        self.vbox_for_key.addLayout(hbox_4)
        self.vbox_for_key.addLayout(hbox_5)
        self.vbox_for_key.addLayout(hbox_btn)
        self.vbox.addLayout(self.vbox_for_key)

        # self.vbox.addSpacing(340)
        # vbox.addItem(QtWidgets.QSpacerItem(0,10,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))

        # ----------- customization window ---------------

        self.setLayout(self.vbox)

        #self.setWindowOpacity(0.8)
        self.resize(1200, 540)
        #self.setStyleSheet("background-color: #ffffff")
        self.stop = False
        self.new_click = False
        thread1 = Thread(target= self.check_keyboard, args=( ), name = 'check_key_thread')
        thread1.start()

    def set_index_device(self):
        object = self.sender()
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=8,channels=2,rate=44100,output=True,
                            input_device_index=None,
                            output_device_index=object.currentIndex())
            self.index_device = object.currentIndex()
            self.label_exception.setText('')
        except Exception as a:
            self.label_exception.setText('  Choose another device')



    def check_keyboard(self):
        keyboard.on_press(self.print_pressed_keys)
        print('test')

    def print_pressed_keys(self,e):
        print(e.name)
        if e.name in self.key_for_audio.keys():
            if self.new_click == True:
                self.stop = True
            else:
                self.stop = False
            self.voise_play(e.name)




    def add_key_in_layout(self, layout, array_key,array_value, spasing):
        if spasing != 0:
            layout.addSpacing(spasing)

        for i in range(len(array_key)):
            if array_key[i] == 'spase':
                layout.addSpacing(array_value[i])
            else:
                self.button = QtWidgets.QPushButton(array_key[i])
                self.button.clicked.connect(self.bind_key)
                self.button.setFixedSize(array_value[i], 30)
                self.button.setStyleSheet("background-color: #ff8000")


                layout.addWidget(self.button)

        layout.addItem(QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, 0))

    def bind_key(self):
        name_button = self.sender()
        file_name = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                    caption="choose audio file",
                                                    filter="Audio file (*.wav)")
        if file_name[0] == '':
            return
        print(file_name)

        cod = name_button.text()
        self.key_for_audio[cod] = file_name[0]
        name_button.setStyleSheet("background-color: #00ff00")


    def voise_play(self,cod_key):
        if self.key_for_audio.get(cod_key,0) == 0:
            return
        name_file  = self.key_for_audio.get(cod_key)
        print('new potock')
        thread = Thread(target= self.play_word, args=(name_file,),name = 'main_thread')
        thread.start()




    def play_word(self,name):

        self.new_click = True


        print(activeCount())
        CHUNK = 1024
        wf = wave.open(name, 'rb')
        p = pyaudio.PyAudio()


        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        input_device_index=None,
                        output_device_index=self.index_device)

        data = wf.readframes(CHUNK)
        print("Start")

        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)
            #print(activeCount())
            count_p = activeCount()
            print(count_p)
            if self.stop == True and count_p >= 5: # bad very bad release
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

"""     
        self.slovar_1 = {'`': 41, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7,
                       '7': 8, '8': 9, '9': 10, '0': 11, '-': 12, '=': 13, 'backspace': 14,
                       'spase': 20,'insert': 82, 'home': 71, 'page up': 73,'spase': 20,
                       'num lock': 69, '/': 53, '*': 55, '-': 74}
        self.slovar_2 = {'tab': 15, 'q': 16, 'w': 17, 'e': 18, 'r': 19, 't': 20, 'y': 21,
                       'u': 22, 'i': 23, 'o': 24, 'p': 25, '[': 26, ']': 27, 'enter': 28,
                       'spase': 20, 'delete': 83, 'end': 79, 'page down': 81, 'spase': 20,
                       'home': 71, 'up': 72, 'page up': 73, '+': 78}
        self.slovar_3 = {'caps lock': 58, 'a': 30, 's': 31, 'd': 32, 'f': 33, 'g': 34,
                       'h': 35,  'j': 36, 'k': 37, 'l': 38, ';': 39, "'": 40, '\\': 43,
                       'spase': 150, 'left': 75, 'clear': 76, 'right': 77, '+': 78}
        self.slovar_4 = {'shift': 42, 'z': 44, 'x': 45, 'c': 46, 'v': 47, 'b': 48, 'n': 49,
                       'm': 50, ',': 51, '.': 52, '/': 53, 'right shift': 54, 'spase': 60,
                       'up': 72, 'spase': 60, 'end': 79, 'down': 80, 'page down': 81, 'enter': 28}
        self.slovar_5 = {'ctrl': 29, 'left windows': 91, 'alt': 56, 'space': 57,
                       'right alt': 56, 'right ctrl': 29, 'spase': 20,'left': 75,
                       'down': 80, 'right': 77, 'spase': 20,'insert': 82, 'delete': 83, 'enter': 28 }
"""
