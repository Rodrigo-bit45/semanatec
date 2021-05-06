import numpy as np
import cv2
import time
import argparse

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-cam', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")
    parser.add_argument('-fb', '--paramFiltroBorroso', default=5, type=int, help="Introduce number value to affect blurryness")
    parser.add_argument('-menu', '--filterMenu', default=0, type=int, help="Introduce filter number")
    
    args = vars(parser.parse_args())
    blurNum = int(args["paramFiltroBorroso"])
    menuNum = int(args["filterMenu"])


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    while cap.isOpened():
        
        #BGR image feed from camera
        success,img = cap.read()
        
        if not success:
            break
        if img is None:
            break
            
        #"Switch case" for filter menu
        if menuNum == 0:
            blur = cv2.GaussianBlur(img, (blurNum,blurNum), 0)
            cv2.imshow("Tu borroso", blur)
        elif menuNum == 1:
            kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
            sepia = cv2.filter2D(img, -1, kernel)
            cv2.imshow("Tu en sepia",sepia)
        elif menuNum == 2:
            im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Tu en blanco y negro", im_gray)
       

        k = cv2.waitKey(10)
        if k==27:
            break


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))



