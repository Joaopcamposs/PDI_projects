from matplotlib import pyplot as plt
import numpy as np
import cv2

#=======================================CRIAÇÃO DE IMAGENS=======================================#
A = np.zeros((300,300))
for i in range(25,175):
    for j in range(125,175):
         A[i][j]=1

plt.subplot(1,3,1), cv2.imshow(" IMAGEM A", A)

B = np.zeros((300,300))
for i in range(125,175):
    for j in range(25,175):
         B[i][j]=1

plt.subplot(1,3,2), cv2.imshow(" IMAGEM B", B)

C = np.zeros((300,300))
for i in range(150,300):
    for j in range(150,300):
         C[i][j]=1

plt.subplot(1,3,3), cv2.imshow(" IMAGEM C", C)

#=======================================CRIAÇÃO DE IMAGENS=======================================#

#=======================================ADIÇÃO=======================================#
#D1 = A+B
#cv2.imshow(" IMAGEM D1 ", D1)
#D2 = B+A
#cv2.imshow(" IMAGEM D2 ", D2)

#E1 = A+C
#cv2.imshow(" IMAGEM E1 ", E1)
#E2 = C+A
#cv2.imshow(" IMAGEM E2 ", E2)

#F1 = B+C
#cv2.imshow(" IMAGEM F1 ", F1)
#F2 = C+B
#cv2.imshow(" IMAGEM F2 ", F2)

#G1 = A+B+C
#cv2.imshow(" IMAGEM G1 ", G1)
#G2 = C+B+A
#cv2.imshow(" IMAGEM G2 ", G2)
#=======================================ADIÇÃO=======================================#

#=======================================SUBTRAÇÃO=======================================#
#D1 = A-B
#cv2.imshow(" IMAGEM D1 ", D1)
#D2 = B-A
#cv2.imshow(" IMAGEM D2 ", D2)

#E1 = A-C
#cv2.imshow(" IMAGEM E1 ", E1)
#E2 = C-A
#cv2.imshow(" IMAGEM E2 ", E2)

#F1 = B-C
#cv2.imshow(" IMAGEM F1 ", F1)
#F2 = C-B
#cv2.imshow(" IMAGEM F2 ", F2)

#G1 = A-B-C
#cv2.imshow(" IMAGEM G1 ", G1)
#G2 = A-C-B
#cv2.imshow(" IMAGEM G2 ", G2)
#G3 = B-A-C
#cv2.imshow(" IMAGEM G3 ", G3)
#G4 = B-C-A
#cv2.imshow(" IMAGEM G4 ", G4)
#G5 = C-A-B
#cv2.imshow(" IMAGEM G5 ", G5)
#G6 = C-B-A
#cv2.imshow(" IMAGEM G6 ", G6)
#=======================================SUBTRAÇÃO=======================================#

#=======================================MULTIPLICAÇÃO=======================================#
#D1 = A*B
#cv2.imshow(" IMAGEM D1 ", D1)
#D2 = B*A
#cv2.imshow(" IMAGEM D2 ", D2)

#E1 = A*C
#cv2.imshow(" IMAGEM E1 ", E1)
#E2 = C*A
#cv2.imshow(" IMAGEM E2 ", E2)

#F1 = B*C
#cv2.imshow(" IMAGEM F1 ", F1)
#F2 = C*B
#cv2.imshow(" IMAGEM F2 ", F2)

#G1 = A*B*C
#cv2.imshow(" IMAGEM G1 ", G1)
#G2 = C*B*A
#cv2.imshow(" IMAGEM G2 ", G2)
#=======================================MULTIPLICAÇÃO=======================================#

#=======================================DIVISÃO=======================================#
#D1 = A/B
#cv2.imshow(" IMAGEM D1 ", D1)
#D2 = B/A
#cv2.imshow(" IMAGEM D2 ", D2)

#E1 = A/C
#cv2.imshow(" IMAGEM E1 ", E1)
#E2 = C/A
#cv2.imshow(" IMAGEM E2 ", E2)

#F1 = B/C
#cv2.imshow(" IMAGEM F1 ", F1)
#F2 = C/B
#cv2.imshow(" IMAGEM F2 ", F2)

#G1 = A/B/C
#cv2.imshow(" IMAGEM G1 ", G1)
#G2 = C/B/A
#cv2.imshow(" IMAGEM G2 ", G2)
#=======================================DIVISÃO=======================================#

cv2.waitKey(0) 




