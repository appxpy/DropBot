'''
https://codereview.stackexchange.com/questions/138992/simple-pyqt5-counting-gui
'''

import sys
import time
import requests
import json
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QFrame, QApplication
from PyQt5.QtCore import pyqtSignal, QObject, QThread
class Worker2(QObject):
    '''
    Class intended to be used in a separate thread to generate numbers and send
    them to another thread.
    '''

    request = pyqtSignal(str)
    stopped = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def run(self):
        '''
        Count from 0 to 99 and emit each value to the GUI thread to display.
        '''
        authform.ui.pushButton.setEnabled(False)
        authform.ui.label.setStyleSheet("color: rgb(255, 185, 21);")
        authform.ui.label.setText('Loading...') 
        apiUrl = 'https://api.dropbot.site/'
        loginArg = authform.ui.login.text()
        passwordArg = authform.ui.password.text()
        finalUrl = apiUrl + '?' + 'login=' + loginArg + '&' + 'password=' + passwordArg
        print('Sending request...')
        req = requests.get(finalUrl)
        print('Request sended')
        data = json.loads(req.text, encoding='utf-8')
        print('Reading response...')
        self.request.emit(str(data))
        self.stopped.emit()


class Application(QMainWindow):
    def startCounting(self):
        if not self.worker2Thread.isRunning():
            self.worker2Thread.start()
    def __init__(self):
        QMainWindow.__init__(self)

        # Configuring widgets        
        self.button = QPushButton()
        self.button.setText('99')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.frame = QFrame()
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)

        # Configuring separate thread
        self.worker2Thread = QThread()
        self.worker2 = Worker2()
        self.worker2.moveToThread(self.worker2Thread)

        # Connecting signals
        self.button.clicked.connect(self.startCounting)
        self.worker2.request.connect(self.button.setText)
        self.worker2.stopped.connect(self.worker2Thread.quit)
        self.worker2Thread.started.connect(self.worker2.run)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())