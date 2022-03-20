# Importaçoes
import cv2
import numpy as np
# Ler a imagem
img = cv2.imread("imagemMoedas.jpeg", 0)
# Declarando o Kernel
kernel = np.ones((5,5),np.uint8)
# Utilizando a limiarização para identificar as moedas
limiar, imgLimiar = cv2.threshold(img, 140, 255,cv2.THRESH_BINARY_INV)
# realizar as operações morfologicas de abertura e fechamento em sequencia
acao = cv2.morphologyEx(imgLimiar,cv2.MORPH_OPEN, kernel)
acao = cv2.morphologyEx(imgLimiar,cv2.MORPH_CLOSE, kernel)
# mostrando as imagens limiarizadas e finalizadas
cv2.imshow("Limiar", imgLimiar)
cv2.imshow("Final", acao)
cv2.waitKey(0)