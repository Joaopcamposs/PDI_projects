import cv2
import numpy as np
from matplotlib import pyplot as plt

# Ler imagem em preto e branco
img = cv2.imread("imagemOriginal_dados.jpg",0)

# Declarar negativo
neg = cv2.bitwise_not(img)

# Declarando o Kernel
kernel = np.ones((10,2),np.uint8)

# Threshold dados
th, dst = cv2.threshold(neg, 23, 255, cv2.THRESH_BINARY);
th, dst2 = cv2.threshold(neg, 215, 255, cv2.THRESH_BINARY);

# correções dados
test = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_DILATE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_DILATE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_DILATE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_DILATE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_CLOSE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_ERODE, kernel)
test = cv2.morphologyEx(test, cv2.MORPH_ERODE, kernel)

# correcoes circulos
test2 = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE, kernel)
test2 = cv2.morphologyEx(test2, cv2.MORPH_DILATE, kernel)
test2 = cv2.morphologyEx(test2, cv2.MORPH_ERODE, kernel)

# Mostrar resultado
cv2.imshow("Final Dados", test)
cv2.imshow("Final Circulos", test2)

cv2.waitKey(0)