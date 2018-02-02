# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main-window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDocuments = QtWidgets.QMenu(self.menubar)
        self.menuDocuments.setObjectName("menuDocuments")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSomething = QtWidgets.QAction(MainWindow)
        self.actionSomething.setEnabled(False)
        self.actionSomething.setObjectName("actionSomething")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setCheckable(False)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMoney = QtWidgets.QAction(MainWindow)
        self.actionMoney.setObjectName("actionMoney")
        self.menuFile.addAction(self.actionSomething)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuDocuments.addAction(self.actionMoney)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDocuments.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDocuments.setTitle(_translate("MainWindow", "Documents"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSomething.setText(_translate("MainWindow", "Something"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionMoney.setText(_translate("MainWindow", "Money"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

