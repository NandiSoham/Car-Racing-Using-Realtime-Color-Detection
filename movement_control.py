import cv2
import numpy as np
import threading
from imutils.video import VideoStream

stop_event = threading.Event()
current_key = []

def image_processing_thread():
    global current_key
    cam = VideoStream(src=0).start()
    cv2.namedWindow("Camera Feed")

    while not stop_event.is_set():
        img = cam.read()
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        value = (11, 11)
        blurred = cv2.GaussianBlur(hsv, value, 0)
        colourLower = np.array([49, 102, 63])
        colourUpper = np.array([180, 255, 255])

        
        height, width = img.shape[:2]

        up_contour = mask[0:height//2, 0:width]
        down_contour = mask[3*height//4:height, 2*width//5:3*width//5]

        key_pressed = False



if __name__ == "__main__":
    