import numpy as np
import cv2
import time
import argparse

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")
    parser.add_argument('-m', '--paramFiltro', default=5, type=int, help="Introduce number value to affect blurryness")

    
    args = vars(parser.parse_args())
    blurNum = int(args["paramFiltro"])


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    while cap.isOpened():
        
        #BGR image feed from camera
        success,img = cap.read()
        
        if not success:
            break
        if img is None:
            break
            
        kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
        
        sharpenKernel = np.array(([[0, -1, 0], [-1, 9, -1], [0, -1, 0]]), np.float32)/9
        sharpen = cv2.filter2D(img, kernel=sharpenKernel, ddepth=-1)
        cv2.imshow("Tu afilado (sharpen)", sharpen)

        sepia1 = cv2.filter2D(img, -1, kernel)
        blur = cv2.GaussianBlur(img, (blurNum,blurNum), 0)
        im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Tu en blanco y negro", im_gray)
        cv2.imshow("Tu borroso", blur)
        cv2.imshow("Tu sepia",sepia1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        cv2.imshow("Tu en caricatura",edges)
        #BGR image feed from camera
        
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


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))



