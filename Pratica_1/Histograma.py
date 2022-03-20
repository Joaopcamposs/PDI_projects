from matplotlib import pyplot as plt
import numpy as np
import cv2

#abre (leitura) uma imagem, transformando ela em uma matriz de pixels
imagem1 = cv2.imread('poker.png',1)
imagem1 = imagem1[::2,::2] # Diminui a imagem

#histograma
cv2.imshow("Imagem Colorida", imagem1)
canais = cv2.split(imagem1) #Separa os canais
grayImagem = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Niveis de Cinza", grayImagem)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cor)
    plt.xlim([0, 256])

hist = cv2.calcHist([grayImagem], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])

plt.show()

#equalização de histograma (na tentativa de melhorar a distribuição dos níveis de cinza e assim aumentar contraste)
img = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)
cv2.imshow('Equalizada',h_eq)
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0) #espera pressionar qualquer tecla
cv2.destroyAllWindows()
