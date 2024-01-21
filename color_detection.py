import cv2
import numpy as np

def create_color_detection_window():
    cv2.namedWindow('Color Detection')
    cv2.createTrackbar('Hue', 'Color Detection', 0, 179, on_trackbar_change)
    cv2.createTrackbar('Saturation', 'Color Detection', 0, 255, on_trackbar_change)
    cv2.createTrackbar('Value', 'Color Detection', 0, 255, on_trackbar_change)

def on_trackbar_change(x):
    pass


def main():
    cap = cv2.VideoCapture(0)
    
if __name__ == "__main__":
    main()
