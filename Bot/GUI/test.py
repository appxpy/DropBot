'''
https://codereview.stackexchange.com/questions/138992/simple-pyqt5-counting-gui
'''

import sys
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QFrame, QApplication
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class Counter(QObject):
    '''
    Class intended to be used in a separate thread to generate numbers and send
    them to another thread.
    '''

    newValue = pyqtSignal(str)
    stopped = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def start(self):
        '''
        Count from 0 to 99 and emit each value to the GUI thread to display.
        '''
        r = 255
        g = 0
        b = 255
        while b != 0:
            b -= 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while r < 255:
            r += 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while g < 255:
            g += 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while r != 0:
            r -= 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while b < 255:
            b += 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while g != 0:
            g -= 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        while r < 255:
            r += 1
            newcolor = str(r) + ',' + str(g) + ',' + str(b)
            self.newValue.emit(str(newcolor))
            time.sleep(.01)
        self.start()
        self.stopped.emit()


class Application(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Configuring widgets        
        self.button = QPushButton()
        self.button.setText('Ебни по мозгам')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.frame = QFrame()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)
        self.frame.setStyleSheet('background-color: black;')
        # Configuring separate thread
        self.counterThread = QThread()
        self.counter = Counter()
        self.counter.moveToThread(self.counterThread)

        # Connecting signals
        self.button.clicked.connect(self.startCounting)
        self.button.setStyleSheet('width: 50px; height: 50px; border-radius: 10px; color: white;')
        self.counter.newValue.connect(self.prikol)
        self.counter.stopped.connect(self.counterThread.quit)
        self.counterThread.started.connect(self.counter.start)

    def prikol(self, newValue):
      print('color: rgb({})'.format(newValue))
      self.frame.setStyleSheet('background-color: rgb({})'.format(newValue))
    def startCounting(self):
        '''
        Start counting if no other counting is done.
        '''

        if not self.counterThread.isRunning():
            self.counterThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())