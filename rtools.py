# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\xu\eric5\Rtools.ui'
#
# Created: Mon Jan 12 19:15:29 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Rtools.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 501, 451))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(0, 0))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.addtab = QtGui.QWidget()
        self.addtab.setObjectName(_fromUtf8("addtab"))
        self.checkBox = QtGui.QCheckBox(self.addtab)
        self.checkBox.setGeometry(QtCore.QRect(100, 50, 111, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.listWidget = QtGui.QListWidget(self.addtab)
        self.listWidget.setGeometry(QtCore.QRect(20, 100, 451, 221))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_5 = QtGui.QLabel(self.addtab)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.addtab)
        self.label.setGeometry(QtCore.QRect(20, 85, 400, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.addtab)
        self.label_2.setGeometry(QtCore.QRect(30, 350, 191, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.addtab)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setGeometry(QtCore.QRect(260, 50, 194, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.addtab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 181, 22))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.toolButton = QtGui.QToolButton(self.addtab)
        self.toolButton.setGeometry(QtCore.QRect(330, 330, 61, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.pushButton = QtGui.QPushButton(self.addtab)
        self.pushButton.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.toolButton_2 = QtGui.QToolButton(self.addtab)
        self.toolButton_2.setGeometry(QtCore.QRect(410, 330, 61, 21))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(self.addtab)
        self.toolButton_3.setGeometry(QtCore.QRect(250, 330, 61, 21))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.lineEdit = QtGui.QLineEdit(self.addtab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 330, 211, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tabWidget.addTab(self.addtab, _fromUtf8(""))
        self.fixtab = QtGui.QWidget()
        self.fixtab.setObjectName(_fromUtf8("fixtab"))
        self.tabWidget.addTab(self.fixtab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 461, 351))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 401, 301))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(0, 460, 531, 23))
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RSAS综合辅助工具", None))
        self.checkBox.setText(_translate("MainWindow", "是否为定时任务", None))
        self.label_5.setText(_translate("MainWindow", "定时任务开始时间：", None))
        self.label.setText(_translate("MainWindow", "待扫URL：[格式:http://www.xxx.com,一行一个]", None))
        self.label_2.setText(_translate("MainWindow", "", None))
        self.label_3.setText(_translate("MainWindow", "任务名称：", None))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>多个同业务名称会后跟类似'~1'来区分</p></body></html>", None))
        self.toolButton.setText(_translate("MainWindow", "导入...", None))
        self.pushButton.setText(_translate("MainWindow", "开始", None))
        self.toolButton_2.setText(_translate("MainWindow", "清空", None))
        self.toolButton_3.setText(_translate("MainWindow", "添加", None))
        self.lineEdit.setText(_translate("MainWindow", "在此处写入URL添加...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addtab), _translate("MainWindow", "批量添加", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fixtab), _translate("MainWindow", "批量修正", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#b9b5ae;\">###############################################</span></p><p align=\"center\"><span style=\" font-weight:600; color:#b9b5ae;\">######## </span><span style=\" font-size:14pt; font-weight:600; color:#b9b5ae;\">RSAS综合辅助工具 </span><span style=\" font-weight:600; color:#b9b5ae;\">########</span></p><p align=\"center\"><span style=\" font-weight:600; color:#b9b5ae;\">###############################################</span></p><p><span style=\" font-weight:600;\"><br/></span></p><p><span style=\" font-size:14pt; font-weight:600; color:#676767;\">版本：0.1</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#676767;\">作者：Techxsh</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#676767;\">博客: </span><a href=\"http://hi.baidu.com/techxsh\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#676767;\">http://hi.baidu.com/techxsh</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "关于辅助", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "备用1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "备用2", None))
        self.menu.setTitle(_translate("MainWindow", "菜单", None))
        self.menu_2.setTitle(_translate("MainWindow", "帮助", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL('clicked()'), self.addUrl)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL('clicked()'), self.clearDialog)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL('clicked()'), self.showDialog)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.exit)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL('clicked()'), self.timeable)
        #self.toolButton.connect(self, self.showDialog(), SIGNAL='clicked()')
    def addUrl(self):
        url = self.lineEdit.text()
        if "http" not in url:
            self.label_2.setText(_translate("MainWindow", "URL格式输入有误！", None))
        else:
            self.listWidget.addItem(url)
            self.label_2.setText(_translate("MainWindow", "", None))
    def exit(self):
        exit()
    def showDialog(self):
        try:
            fname = QtGui.QFileDialog.getOpenFileName()
            f = open(fname, 'r')
            datas = f.readlines()
            #print(data)
            count = 0
            progressValue = len(datas)
            for data in datas:
                count += 1
                progressValue = count/len(datas) * 100
                self.progressBar.setValue(progressValue)
                self.listWidget.addItem(data)
        except:
            print("wrong")
    def clearDialog(self):
        self.listWidget.clear()
    def about(self):
        self.tabWidget.setCurrentIndex(4)
    def timeable(self):
        #print(self.checkBox.isChecked())
        if self.checkBox.isChecked() == True:
            self.dateTimeEdit.setEnabled(True)
        else:
            self.dateTimeEdit.setEnabled(False)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

