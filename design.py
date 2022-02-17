'''
Программа калькулятор
Краснов Леонид ИУ7-21Б
'''

import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMenuBar, QMenu, QApplication
from PyQt6.QtGui import QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Создание меню и главных вкладок
        self.menubar = MainWindow.menuBar()
        self.Clean = self.menubar.addMenu('Чистка')
        self.Action = self.menubar.addMenu('Действия')
        self.About = self.menubar.addMenu('О программе')

        # Создание подвкладок
        self.CleanAll = QAction('Очистить все поля', MainWindow)
        self.CleanTextField = QAction('Очистить поле ввода', MainWindow)
        self.CleanAllTextField = QAction('Очистить поля вывода', MainWindow)

        self.Rezult = QAction('Результат', MainWindow)
        self.Translate = QAction('Перевод', MainWindow)

        self.Prog = QAction('О программе', MainWindow)
        self.Autor = QAction('Автор', MainWindow)

        # Размещение подвкладок
        self.Clean.addAction(self.CleanAll)
        self.Clean.addAction(self.CleanTextField)
        self.Clean.addAction(self.CleanAllTextField)

        self.Action.addAction(self.Rezult)
        self.Action.addAction(self.Translate)

        self.About.addAction(self.Prog)
        self.About.addAction(self.Autor)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: #E8805D;")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(260, 150, 111, 30))
        self.input1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input1.setObjectName("input1")

        self.input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(480, 150, 110, 30))
        self.input2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input2.setObjectName("input2")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(379, 150, 91, 30))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(480, 300, 110, 30))
        self.btn_3.setStyleSheet("background-color: #FFD89E")
        self.btn_3.setObjectName("btn_3")

        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(370, 300, 110, 30))
        self.btn_2.setStyleSheet("background-color: #FFD89E")
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(260, 300, 110, 30))
        self.btn_1.setStyleSheet("background-color: #FFD89E")
        self.btn_1.setObjectName("btn_1")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(480, 270, 110, 30))
        self.btn_6.setStyleSheet("background-color: #FFD89E")
        self.btn_6.setObjectName("btn_6")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(370, 270, 110, 30))
        self.btn_5.setStyleSheet("background-color: #FFD89E")
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(260, 270, 110, 30))
        self.btn_4.setStyleSheet("background-color: #FFD89E")
        self.btn_4.setObjectName("btn_4")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(480, 240, 110, 30))
        self.btn_9.setStyleSheet("background-color: #FFD89E")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(370, 240, 110, 30))
        self.btn_8.setStyleSheet("background-color: #FFD89E")
        self.btn_8.setObjectName("btn_8")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(260, 240, 110, 30))
        self.btn_7.setStyleSheet("background-color: #FFD89E")
        self.btn_7.setObjectName("btn_7")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(260, 330, 110, 30))
        self.btn_0.setStyleSheet("background-color: #FFD89E")
        self.btn_0.setObjectName("btn_0")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(260, 90, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(255, 233, 183)")
        self.label_result.setObjectName("label_result")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(370, 330, 110, 30))
        self.btn_minus.setStyleSheet("background-color: #FFD89E")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setGeometry(QtCore.QRect(480, 330, 110, 30))
        self.btn_point.setStyleSheet("background-color: #FFD89E")
        self.btn_point.setObjectName("btn_point")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(390, 190, 61, 20))
        self.radioButton.setStyleSheet("background-color: rgb(255, 238, 105);")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 210, 61, 20))
        self.radioButton_2.setStyleSheet("background-color: rgb(255, 238, 105);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.labele_6a_to_10a = QtWidgets.QLabel(self.centralwidget)
        self.labele_6a_to_10a.setGeometry(QtCore.QRect(60, 60, 531, 20))
        self.labele_6a_to_10a.setStyleSheet("background-color: rgb(235, 255, 177);")
        self.labele_6a_to_10a.setObjectName("labele_6a_to_10a")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 90, 191, 271))
        self.tabWidget.setStyleSheet("background-color: rgb(178, 155, 100);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_clean_3 = QtWidgets.QPushButton(self.tab)
        self.btn_clean_3.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.btn_clean_3.setStyleSheet("background-color: rgb(255, 70, 0);")
        self.btn_clean_3.setObjectName("btn_clean_3")
        self.btn_clean = QtWidgets.QPushButton(self.tab)
        self.btn_clean.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.btn_clean.setStyleSheet("background-color: rgb(255, 70, 0);")
        self.btn_clean.setObjectName("btn_clean")
        self.btn_clean_2 = QtWidgets.QPushButton(self.tab)
        self.btn_clean_2.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.btn_clean_2.setStyleSheet("background-color: rgb(255, 70, 0);")
        self.btn_clean_2.setObjectName("btn_clean_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_rez = QtWidgets.QPushButton(self.tab_2)
        self.btn_rez.setGeometry(QtCore.QRect(40, 20, 110, 30))
        self.btn_rez.setStyleSheet("background-color: rgb(169, 255, 0);")
        self.btn_rez.setObjectName("btn_rez")
        self.translate = QtWidgets.QPushButton(self.tab_2)
        self.translate.setGeometry(QtCore.QRect(40, 60, 111, 32))
        self.translate.setStyleSheet("background-color: rgb(255, 224, 0);")
        self.translate.setObjectName("translate")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(0, 1, 191, 251))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.add_functions()



    #  Функция для подписывания элементов
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Краснов Леонид [ИУ7-21Б]"))
        self.input1.setText(_translate("MainWindow", "Введите число 1"))
        self.input2.setText(_translate("MainWindow", "Введите число 2"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.label_result.setText(_translate("MainWindow", "результат действия"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.radioButton.setText(_translate("MainWindow", "Поле1"))
        self.radioButton_2.setText(_translate("MainWindow", "Поле2"))
        self.labele_6a_to_10a.setText(
            _translate("MainWindow", "Здесь отображаетсячисло, переведенное из 6-й в 10-ую"))
        self.btn_clean_3.setText(_translate("MainWindow", "Очистить все поля"))
        self.btn_clean.setText(_translate("MainWindow", "Очистить поле ввода"))
        self.btn_clean_2.setText(_translate("MainWindow", "Очистить поля вывода"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Чистка"))
        self.btn_rez.setText(_translate("MainWindow", "Результат"))
        self.translate.setText(_translate("MainWindow", "Перевод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Действия"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор:</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Краснов Леонид [ИУ7-11Б]</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Программа:</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Калькулятор, выполняющий простые арифметические действия, с возможностью перевода результата в 6-ю систему счисления и обратно.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Автор"))

    #  Функция для бинда элементов
    def add_functions(self):
        self.CleanAll.triggered.connect(lambda: self.clean_all())
        self.CleanAllTextField.triggered.connect(lambda: self.clean_output())
        self.CleanTextField.triggered.connect(lambda: self.clean_field())

        self.Rezult.triggered.connect(lambda: self.getresult())
        self.Translate.triggered.connect(lambda: self.translator())

        self.Prog.triggered.connect(lambda: self.progmessage())
        self.Autor.triggered.connect(lambda: self.autormessage())

        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_point.clicked.connect(lambda: self.write_number(self.btn_point.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))

        self.btn_rez.clicked.connect(lambda: self.getresult())
        self.translate.clicked.connect(lambda: self.translator())

        self.btn_clean_2.clicked.connect(lambda: self.clean_output())
        self.btn_clean_3.clicked.connect(lambda: self.clean_all())
        self.btn_clean.clicked.connect(lambda: self.clean_field())

    def progmessage(self):
        message = QtWidgets.QMessageBox()
        message.setText("Калькулятор, выполняющий простые арифметические действия, с возможностью перевода результата в"
                        " 6 -ю систему счисления и обратно.")
        message.exec()


    def autormessage(self):
        message = QtWidgets.QMessageBox()
        message.setText("Автор программы:\nКраснов Леонид [ИУ7-11Б]")
        message.exec()


    #  Функця для ввода числа с виртуальной клавиатуры
    def write_number(self, number):
        if self.radioButton.isChecked():
            self.input1.setText(self.input1.text() + number)
        elif self.radioButton_2.isChecked():
            self.input2.setText(self.input2.text() + number)

    #  Функция для очищения выбранной области
    def clean_field(self):
        if self.radioButton.isChecked():
            self.input1.setText("")
        elif self.radioButton_2.isChecked():
            self.input2.setText("")

    #  Функция для вычисления результата
    def getresult(self):
        a = self.input1.text()
        b = self.input2.text()
        try:
            a = float(a)
        except:
            message = QtWidgets.QMessageBox()
            message.setText("Неверный ввод первого числа!")
            message.exec()
            return 1
        try:
            b = float(b)
        except:
            message = QtWidgets.QMessageBox()
            message.setText("Неверный ввод второго числа!")
            message.exec()
        try:
            if a != "" and b != "":
                if self.comboBox.currentText() == "+":
                    rez = a + b
                elif self.comboBox.currentText() == "-":
                    rez = a - b
                elif self.comboBox.currentText() == "*":
                    rez = a * b
                elif self.comboBox.currentText() == "/":
                    try:
                        rez = a / b
                        rez = str(rez)
                    except:
                        message = QtWidgets.QMessageBox()
                        message.setText("Порытка деления на 0!")
                        message.exec()
                        return 0
                self.label_result.setText(str(rez))
            else:
                message = QtWidgets.QMessageBox()
                message.setText("Одно из полей пусто!")
                message.exec()
        except:
            message = QtWidgets.QMessageBox()
            message.setText("Одно из полей заполнено неверно!")
            message.exec()

    def translator(self):
        a = self.label_result.text()
        try:
            a = transform10to6(a)
            self.label_result.setText(str(a))
            a = str(a)
            a = transformto10(a)
            print(a)
            self.labele_6a_to_10a.setText(str(a))
        except:
            message = QtWidgets.QMessageBox()
            message.setText("Скорее всего вы не нажали на кнопку 'Результат'")
            message.exec()

    #  Функция чистит окно вывода
    def clean_output(self):
        self.label_result.setText("")
        self.labele_6a_to_10a.setText("")

    # Функция чистит все окна в программе
    def clean_all(self):
        self.clean_output()
        self.input1.setText("")
        self.input2.setText("")


#  Функция для перевода из 10 в 6-ю систему счисления
def transform10to6(num):
    minus = 0
    if '-' in num:
        minus = 1
        num = num.replace("-", "")
    savenum = num
    beforpoint = ""
    i = 0
    if "." in num:
        while savenum[i] != '.':
            beforpoint += savenum[i]
            i += 1
        beforpoint += savenum[i]
    else:
        beforpoint = savenum
        num = "0.0"
    if num != "0.0":
        num = "0." + num.replace(beforpoint, "")
    else:
        num = 0
    rem = float(num)
    beforpoint = float(beforpoint)
    beforpoint = int(beforpoint)
    step = 6
    rems = []
    liters = {
        "0": "0",
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5'
    }
    while beforpoint >= step:
        rems.append(beforpoint % step)
        beforpoint //= step
    rems.append(beforpoint % step)
    rems.reverse()
    beforpoint = ""
    for i in range(len(rems)):
        beforpoint += liters[str(rems[i])]

    rems = []
    while rem > 0:
        torems = rem * 6
        rem = int(torems)
        rems.append(rem)
        rem = torems - rem

    afterpoint = ""
    for i in range(len(rems)):
        afterpoint += liters[str(rems[i])]
    if afterpoint != "":
        rez = beforpoint + "." + afterpoint
        rez = float(rez)
        if minus == 1:
            rez *= -1
        return rez
    else:
        if minus == 1:
            beforpoint *= -1
        return beforpoint


#  Функция для перевода из 6-ой системы счисления в десятичную
def transformto10(num):
    num = str(num)
    minus = 0
    if '-' in num:
        minus = 1
        num = num.replace("-", "")
    i = 0
    if "." in num:
        while num[i] != ".":
            i += 1
        i -= 1
    else:
        i = len(num) - 1
    tennum = 0
    for j in range(len(num)):
        if num[j] != ".":
            tennum = tennum + (int(num[j]) * 6 ** i)
            i -= 1
    if minus == 1:
        tennum *= -1
    return tennum
