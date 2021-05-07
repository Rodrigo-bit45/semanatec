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
        

        k = cv2.waitKey(10)
        if k==27:
            break


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))



