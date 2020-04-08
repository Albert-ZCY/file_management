from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 378)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(210, 10, 121, 27))
        font1 = QFont()
        font1.setFamily(u"\u6977\u4f53")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.name.setFont(font1)
        self.choice_3 = QPushButton(self.centralwidget)
        self.choice_3.setObjectName(u"choice_3")
        self.choice_3.setGeometry(QRect(330, 180, 131, 151))
        font2 = QFont()
        font2.setFamily(u"\u4eff\u5b8b")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.choice_3.setFont(font2)
        self.choice_2 = QPushButton(self.centralwidget)
        self.choice_2.setObjectName(u"choice_2")
        self.choice_2.setGeometry(QRect(200, 180, 131, 151))
        self.choice_2.setFont(font2)
        self.choice_1 = QPushButton(self.centralwidget)
        self.choice_1.setObjectName(u"choice_1")
        self.choice_1.setGeometry(QRect(70, 180, 131, 151))
        self.choice_1.setFont(font2)
        self.Ename = QLabel(self.centralwidget)
        self.Ename.setObjectName(u"Ename")
        self.Ename.setGeometry(QRect(200, 40, 135, 16))
        font3 = QFont()
        font3.setFamily(u"\u4eff\u5b8b")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.Ename.setFont(font3)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 511, 74))
        self.text = QVBoxLayout(self.widget)
        self.text.setObjectName(u"text")
        self.text.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"\u4eff\u5b8b")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_3.setFont(font4)

        self.text.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.text.addItem(self.verticalSpacer)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.text.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.text.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.text.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 531, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.choice_3.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u5907\u4efd", None))
        self.choice_2.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u6e05\u7406", None))
        self.choice_1.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u6574\u7406", None))
        self.Ename.setText(QCoreApplication.translate("MainWindow", u"file management", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u6587\u4ef6\u7ba1\u7406!\u60a8\u53ef\u4ee5\u4f7f\u7528\u672c\u7a0b\u5e8f\u5feb\u901f\u9ad8\u6548\u7684\u5206\u7c7b\u3001\u6e05\u7406\u3001\u5907\u4efd\u6587\u4ef6\uff0c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u60a8\u7684\u6587\u4ef6\u5939\u66f4\u52a0\u6574\u6d01\u3001\u7cbe\u7b80\u3001\u5b89\u5168\u3002", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u60a8\u9700\u8981\u7684\u64cd\u4f5c\u6a21\u5757\uff1a", None))
    # retranslateUi