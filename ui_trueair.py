# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trueair.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(404, 431)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.source = QLabel(self.centralwidget)
        self.source.setObjectName(u"source")

        self.gridLayout_2.addWidget(self.source, 0, 0, 1, 1)

        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setObjectName(u"calendar")

        self.gridLayout_2.addWidget(self.calendar, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.span = QComboBox(self.centralwidget)
        self.span.setObjectName(u"span")

        self.horizontalLayout_2.addWidget(self.span)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonFrom = QPushButton(self.centralwidget)
        self.buttonFrom.setObjectName(u"buttonFrom")

        self.verticalLayout.addWidget(self.buttonFrom)

        self.buttonTo = QPushButton(self.centralwidget)
        self.buttonTo.setObjectName(u"buttonTo")

        self.verticalLayout.addWidget(self.buttonTo)

        self.buttonPlot = QPushButton(self.centralwidget)
        self.buttonPlot.setObjectName(u"buttonPlot")

        self.verticalLayout.addWidget(self.buttonPlot)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.fitType = QComboBox(self.centralwidget)
        self.fitType.setObjectName(u"fitType")

        self.horizontalLayout.addWidget(self.fitType)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.startdate = QLabel(self.centralwidget)
        self.startdate.setObjectName(u"startdate")

        self.verticalLayout_2.addWidget(self.startdate)

        self.enddate = QLabel(self.centralwidget)
        self.enddate.setObjectName(u"enddate")

        self.verticalLayout_2.addWidget(self.enddate)

        self.note = QLabel(self.centralwidget)
        self.note.setObjectName(u"note")

        self.verticalLayout_2.addWidget(self.note)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 404, 21))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addAction(self.actionClose)
        self.menuFIle.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.source.setText(QCoreApplication.translate("MainWindow", u"No database selected", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Span", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Days", None))
        self.buttonFrom.setText(QCoreApplication.translate("MainWindow", u"Select Start Date", None))
        self.buttonTo.setText(QCoreApplication.translate("MainWindow", u"Select End Date", None))
        self.buttonPlot.setText(QCoreApplication.translate("MainWindow", u"Plot Blood Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data fit type:", None))
        self.startdate.setText(QCoreApplication.translate("MainWindow", u"No start date selected", None))
        self.enddate.setText(QCoreApplication.translate("MainWindow", u"No end date selected", None))
        self.note.setText(QCoreApplication.translate("MainWindow", u"Select a database", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

