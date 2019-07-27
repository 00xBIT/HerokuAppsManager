import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextEdit, QComboBox

import manager

class Example(QWidget):
    __manager = None
    __qcbAccounts = None
    __qcbApps = None

    def __init__(self, manager):
        self.__manager = manager
        self.__qte = None

        super().__init__()
        
        hbox = QHBoxLayout(self)

        vbox = QVBoxLayout(self)
        hbox.addLayout(vbox)

        # lb = QLabel(self)
        # lb.setText('Menu:')
        # vbox.addWidget(lb)

        qpbReadConfig = QPushButton('Read Config', self)
        qpbReadConfig.clicked.connect(self.readConfig)
        vbox.addWidget(qpbReadConfig)

        self.__qcbAccounts = QComboBox(self)
        vbox.addWidget(self.__qcbAccounts)

        qpbReadConfig = QPushButton('Connect', self)
        qpbReadConfig.clicked.connect(self.connect)
        vbox.addWidget(qpbReadConfig)

        self.__qcbApps = QComboBox(self)
        vbox.addWidget(self.__qcbApps)

        lbProcess = QLabel(self)
        lbProcess.setText('Process:')
        vbox.addWidget(lbProcess)

        qhlProcess = QHBoxLayout()
        vbox.addLayout(qhlProcess)

        qpbStart = QPushButton('Start', self)
        qpbStart.clicked.connect(self.start)
        qhlProcess.addWidget(qpbStart)

        qpbStop = QPushButton('Stop', self)
        qpbStop.clicked.connect(self.stop)
        qhlProcess.addWidget(qpbStop)

        lbMaintenanceMode = QLabel(self)
        lbMaintenanceMode.setText('Maintenance Mode:')
        vbox.addWidget(lbMaintenanceMode)

        qhlMaintenanceMode = QHBoxLayout()
        vbox.addLayout(qhlMaintenanceMode)

        qpbEnable = QPushButton('Enable maintenance', self)
        qpbEnable.clicked.connect(self.enable)
        qhlMaintenanceMode.addWidget(qpbEnable)

        qpbDisable = QPushButton('Disable maintenance', self)
        qpbDisable.clicked.connect(self.disable)
        qhlMaintenanceMode.addWidget(qpbDisable)

        # qpbStop = QPushButton('Test', self)
        # qpbStop.clicked.connect(self.test)
        # vbox.addWidget(qpbStop)
        
        # self.__qte = QTextEdit(self)
        # vbox.addWidget(self.__qte)

        self.setLayout(hbox)

    def readConfig(self):
        self.__qcbAccounts.clear()
        self.__manager.readConfig()

        for name in self.__manager.accountsNames():
            self.__qcbAccounts.addItem(name)

    def connect(self):
        self.__qcbApps.clear()

        index = self.__qcbAccounts.currentIndex()
        self.__manager.authenticate(self.__manager.accountsNames()[index])

        for name in self.__manager.getAppsNames():
            self.__qcbApps.addItem(name)
        
        # for appName in self.__manager.getAppsNames():
        #     self.__qte.setText(self.__qte.toPlainText() + appName + '\r\n')

    def start(self):
        index = self.__qcbApps.currentIndex()
        self.__manager.appStart(self.__manager.getAppsNames()[index])

    def stop(self):
        index = self.__qcbApps.currentIndex()
        self.__manager.appStop(self.__manager.getAppsNames()[index])

    def enable(self):
        index = self.__qcbApps.currentIndex()
        self.__manager.enableMaintenanceMode(self.__manager.getAppsNames()[index])

    def disable(self):
        index = self.__qcbApps.currentIndex()
        self.__manager.disableMaintenanceMode(self.__manager.getAppsNames()[index])

    def test(self):
        index = self.__qcbApps.currentIndex()
        self.__manager.test(self.__manager.getAppsNames()[index])

    

class Window():
    __manager = None

    def __init__(self, manager):
        self.__manager = manager
        app = QApplication(sys.argv)
    
        w = Example(self.__manager)
        w.resize(500, 300)
        # w.move(300, 300)
        w.setWindowTitle('HerokuAppsManager')
        w.show()

        sys.exit(app.exec_())