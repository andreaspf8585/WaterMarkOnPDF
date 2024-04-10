from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyPDF4 import PdfFileWriter, PdfFileReader
import PyPDF4
from PyQt6.QtWidgets import QMessageBox
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 284)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WaterMarkOnPDF - Andreas Gkogkos"))
        self.label.setText(_translate("MainWindow", "Filename path"))
        self.label_2.setText(_translate("MainWindow", "Filename path"))
        self.lineEdit_2.setText(_translate("MainWindow", "Folder path"))
        self.label_3.setText(_translate("MainWindow", "Watermark pdf path"))
        self.pushButton.setText(_translate("MainWindow", "Add watermark on PDF"))
        self.pushButton.clicked.connect(self.applyWaterMark)
        self.lineEdit.textChanged.connect(self.deleteTextFromSecondLineEdit)
        self.lineEdit_2.textChanged.connect(self.deleteTextFromFirstLineEdit)
        self.label_2.setText("Folder path")
        self.lineEdit_2.setText("")

    def applyWaterMark(self):
        input_pdf = self.lineEdit.text()
        folder_path = self.lineEdit_2.text()

        if len(input_pdf) > 0:
            output_pdf = input_pdf
            output_pdf = output_pdf.replace(".pdf", "WithWatermark.pdf")
            watermark = self.lineEdit_3.text()
            PyPDF4.PdfFileReader(input_pdf)
            self.put_watermark(input_pdf, output_pdf, watermark)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            dlg = QMessageBox()
            dlg.setWindowTitle("")
            dlg.setText("File " + output_pdf + " created successfully!!!")
            dlg.show()
            button = dlg.exec()
        if len(folder_path) > 0:
            fileList = os.listdir(self.lineEdit_2.text())
            pdfList = []
            for file in fileList:
                if ".pdf" in file or ".PDF" in file:
                    pdfList.append(file)
            print(pdfList)
            for file in pdfList:
                input_pdf = file
                output_pdf = input_pdf
                output_pdf = output_pdf.replace(".pdf", "WithWatermark.pdf")
                watermark = self.lineEdit_3.text()
                PyPDF4.PdfFileReader(input_pdf)
                self.put_watermark(input_pdf, output_pdf, watermark)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            dlg = QMessageBox()
            dlg.setWindowTitle("")
            dlg.setText("Watermarks created successfully !!!")
            dlg.show()
            button = dlg.exec()

    def put_watermark(self, input_pdf, output_pdf, watermark):
        watermark_instance = PdfFileReader(watermark)
        watermark_page = watermark_instance.getPage(0)
        pdf_reader = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)
        with open(output_pdf, 'wb') as out:
            pdf_writer.write(out)

    def deleteTextFromFirstLineEdit(self):
        self.lineEdit.setText("")

    def deleteTextFromSecondLineEdit(self):
        self.lineEdit_2.setText("")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
