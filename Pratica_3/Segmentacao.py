# Biblioteca principal: OpenCV.
import cv2 as opencv
import numpy as np

# Carregando imagem.
imagem = opencv.imread('imagemMoedas.jpeg')

# Mostrando imagem.
opencv.imshow('Imagem original', imagem)

# Criando imagem em tons de cinza.
imagem_grey_scale = opencv.cvtColor(imagem, opencv.COLOR_BGR2GRAY)

# Aplicando filtro de média.
imagem_grey_scale = opencv.medianBlur(imagem_grey_scale, 5)

# Mostrando imagem em tons de cinza.
opencv.imshow('Imagem em tons de cinza', imagem_grey_scale)
opencv.imwrite('imagem_tons_cinza.png', imagem_grey_scale)

altura = imagem_grey_scale.shape[0]
circulos = opencv.HoughCircles(imagem_grey_scale, opencv.HOUGH_GRADIENT, 1, altura/8, param1=100, param2=30, minRadius=1, maxRadius=100)

if circulos is not None:
    imagem[:] = (0, 0, 0)
    circulos = np.uint16(np.around(circulos))
    indicador_desafio = 0
    for i in circulos[0, :]:
        indicador_desafio += 1
        #if indicador_desafio != 3:
        print("Desenhando círculo! ", i)
        centro = (i[0], i[1])
        opencv.circle(imagem, centro, 1, (255, 255, 255), -1)
        raio = i[2]
        opencv.circle(imagem, centro, raio, (255, 255, 255), -1)

# Mostrando a imagem com circulos detectados.
opencv.imshow('Circulos Detectados', imagem)
opencv.imwrite('circulos_detectados.png', imagem)

opencv.waitKey(0)