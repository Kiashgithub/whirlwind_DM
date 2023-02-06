# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"QWidget{background-color:rgb(149, 0, 255);\n"
"}")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 170, 75, 24))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 85, 0);\n"
"}")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(162, 90, 421, 22))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(211, 211, 211);\n"
"}")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 40, 431, 20))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"color:rgb(182, 182, 178);\n"
"	font: 900 16pt \"Arial Black\";\n"
"}")
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(162, 130, 421, 22))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(211, 211, 211);\n"
"}")
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(320, 210, 151, 23))
        self.progressBar.setValue(0)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 170, 75, 24))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(255, 161, 67);\n"
"}")
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 170, 75, 24))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(170, 0, 0);\n"
"}")
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(370, 170, 75, 24))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(85, 170, 0);\n"
"}")
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(210, 240, 321, 192))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"color:rgb(85, 255, 0);\n"
"background-color:rgb(0, 0, 0);\n"
"}")
        self.textBrowser.setFrameShadow(QFrame.Sunken)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"WhirlWind Download Manager (WDM)", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Download Link", None))
        self.label.setText(QCoreApplication.translate("Widget", u"WhirlWind Download Manager (WDM)", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"File Path", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Pause", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Resume", None))
    # retranslateUi

