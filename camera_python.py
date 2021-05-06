import cv2
import time
import argparse

#Equipo 2: bla bla bla

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

        blur = cv2.GaussianBlur(img, (blurNum,blurNum), 0)
        
        cv2.imshow("Output", blur)

        k = cv2.waitKey(10)
        if k==27:
            break


    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))


