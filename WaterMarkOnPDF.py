from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyPDF4 import PdfFileWriter, PdfFileReader
import PyPDF4
from PyQt6.QtWidgets import QMessageBox
import os
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QFileInfo




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 349)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WatermarkOnPdf - GKOGKOS ANDREAS"))
        self.label.setText(_translate("MainWindow", "PDF file path:"))
        self.pushButton.setText(_translate("MainWindow", "... or choose file"))
        self.label_2.setText(_translate("MainWindow", "PDF files folder path:"))
        self.pushButton_2.setText(_translate("MainWindow", "... or choose folder"))
        self.label_3.setText(_translate("MainWindow", "Watermark PDF file path:"))
        self.pushButton_3.setText(_translate("MainWindow", "... or choose file"))
        self.pushButton_4.setText(_translate("MainWindow", "ADD WATERMARK"))
        self.lineEdit.textChanged.connect(self.clearFolderTextField)
        self.lineEdit_2.textChanged.connect(self.clearPdfFilePathTextField)
        self.pushButton_4.clicked.connect(self.applyWaterMark)
        self.pushButton.clicked.connect(self.openFileDialog)
        self.pushButton_2.clicked.connect(self.openFolderDialog)
        self.pushButton_3.clicked.connect(self.openWatermarkFileDialog)

    def clearFolderTextField(self):
        self.lineEdit_2.setText("")

    def clearPdfFilePathTextField(self):
        self.lineEdit.setText("")

    def clearWaterMarkFilePathTextField(self):
        self.lineEdit_3.setText("")

    def applyWaterMark(self):
        input_pdf = self.lineEdit.text()
        folder_path = self.lineEdit_2.text()

        if len(input_pdf) > 0:
            output_pdf = input_pdf
            output_pdf = output_pdf.replace(".pdf", "_NEW.pdf")
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
                print("Applying watermark on file: " + file)
                input_pdf = file
                output_pdf = input_pdf
                output_pdf = output_pdf.replace(".pdf", "_NEW.pdf")
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

    def openFileDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Select PDF File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            print(selected_files)
            self.clearPdfFilePathTextField()
            self.clearFolderTextField()
            self.lineEdit.setText(str(selected_files[0]))

    def openFolderDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Select PDF File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0]
            file_info = QFileInfo(file_path)
            folder_path = file_info.absolutePath()
            self.clearPdfFilePathTextField()
            self.clearFolderTextField()
            self.lineEdit_2.setText(folder_path)

    def openWatermarkFileDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Select PDF File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            print(selected_files)
            self.lineEdit_3.setText(str(selected_files[0]))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
