import cv2
import numpy as np

img = cv2.imread('imgDadosRoteiro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img,100,200)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)

# Salvar Imagens
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Original.jpg',small)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\SobelHorizontal.jpg',sobelx)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\SobelVertical.jpg',sobely)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Sobel.jpg',sobel)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Laplace.jpg',laplace)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Canny.jpg',canny)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Prewittx.jpg',prewittx)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Prewitty.jpg',prewitty)
# cv2.imwrite('D:\IFTM\8-SEM\PDI\Trabalho s13\Prewitt.jpg',prewittx + prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()