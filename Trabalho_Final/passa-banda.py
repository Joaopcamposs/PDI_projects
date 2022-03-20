import sys
import cv2
import numpy

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def abrirImagem(self):
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Buscar imagem', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
            if filename:
                with open(filename, "rb") as file:
                    data = numpy.array(bytearray(file.read()))

                    self.image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
                    # self.image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                    self.mostrarImagem()
                    self.mostrarImagemOriginal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrir.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnAbrir.clicked.connect(self.abrirImagem)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 80, 371, 291))
        self.openGLWidget.setObjectName("openGLWidget")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget_2.setGeometry(QtCore.QRect(400, 80, 381, 291))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 10, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 10, 141, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.btnAplicar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAplicar.setGeometry(QtCore.QRect(680, 10, 101, 31))
        self.btnAplicar.setObjectName("btnAplicar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiltro_passa_banda = QtWidgets.QMenu(self.menubar)
        self.menuFiltro_passa_banda.setObjectName("menuFiltro_passa_banda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFiltro_passa_banda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAbrir.setText(_translate("MainWindow", "Abrir imagem..."))
        self.label.setText(_translate("MainWindow", "Largura central:"))
        self.label_2.setText(_translate("MainWindow", "Frequencia:"))
        self.btnAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.menuFiltro_passa_banda.setTitle(_translate("MainWindow", "Filtro passa banda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
