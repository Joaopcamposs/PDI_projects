import sys
import cv2
import numpy

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QSlider, QWidget, QLineEdit, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.label = QLabel()
        self.original = QLabel()
        self.textbox = QLineEdit()
        self.textboxFC = QLineEdit()
        self.textboxLB = QLineEdit()
        self.initUI()

    def initUI(self):
        btn_open = QPushButton('Abrir imagem...')
        btn_open.clicked.connect(self.abrirImagem)

        self.textbox = QLineEdit(self)
        self.textbox.setText('0')
        self.namelabel = QLabel(self)
        self.namelabel.setText('Parametro de threshold: ')

        btn_processar = QPushButton('Limiarização')
        btn_processar.clicked.connect(self.limiarizacao)

        self.textboxFC = QLineEdit(self)
        self.textboxFC.setText('0')
        self.namelabelFC = QLabel(self)
        self.namelabelFC.setText('Frequencia central: ')

        self.textboxLB = QLineEdit(self)
        self.textboxLB.setText('0')
        self.namelabelLB = QLabel(self)
        self.namelabelLB.setText('Frequencia central: ')

        
        self.label.setText('Imagem')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('border: gray; border-style:solid; border-width: 1px;')

        self.original.setText('Imagem Original')
        self.original.setAlignment(Qt.AlignCenter)
        self.original.setStyleSheet('border: gray; border-style:solid; border-width: 1px;')

        top_bar = QHBoxLayout()
        top_bar.addWidget(btn_open)
        top_bar.addWidget(btn_processar)
        top_bar.addWidget(self.namelabel)
        top_bar.addWidget(self.textbox)
        top_bar.addWidget(self.textboxFC)

        root = QVBoxLayout(self)
        root.addLayout(top_bar)
        root.addWidget(self.original)
        root.addWidget(self.label)

        self.resize(540, 574)
        self.setWindowTitle('Trabalho Final')

    def abrirImagem(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Buscar imagem', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if filename:
            with open(filename, "rb") as file:
                data = numpy.array(bytearray(file.read()))

                self.image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
                self.mostrarImagem()
                self.mostrarImagemOriginal()

    def limiarizacao(self):
        if self.image is not None:

            imgaux = self.image
            textboxValue = self.textbox.text()

            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            limiar, self.image = cv2.threshold(self.image,int(textboxValue), 255, cv2.THRESH_BINARY_INV)

            self.mostrarImagem()
            self.image = imgaux


    def mostrarImagem(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8


        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.label.setPixmap(QPixmap.fromImage(img))
        self.resize(self.label.pixmap().size())


    def mostrarImagemOriginal(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8


        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()


        self.original.setPixmap(QPixmap.fromImage(img))
        self.resize(self.original.pixmap().size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())