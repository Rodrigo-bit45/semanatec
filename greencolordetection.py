import cv2
import numpy as np

cap = cv2.VideoCapture(0) #0 local or primary camera

while cap.isOpened():
   
        #BGR image feed from camera
    ret, img = cap.read()
    #Lea la imagen y conviértala en HSV usando cvtColor():
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Ahora se crea una matriz NumPy para los valores verdes inferiores y los valores verdes superiores:
    lower_green = np.array([34, 177, 76])
    upper_green = np.array([255, 255, 255])
    
    #Se utiliza el método inRange() de cv2 para comprobar si los elementos de la matriz de imágenes dados se encuentran entre los valores de la matriz de los límites superiores e inferiores:
    masking = cv2.inRange(hsv_img, lower_green, upper_green)    #Esto detectará el color verde.

    #Por último, se muestra las imágenes originales y las resultantes:

    cv2.imshow("Original Image", img)

    cv2.imshow("Green Color detection", masking)

    k = cv2.waitKey(10)
    if k==27:
        break