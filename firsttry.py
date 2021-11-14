import numpy as np
import cv2
frame = cv2.imread("ssstkizkulesi.jpg",0)

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_white = np.array([0 , 0 ,100])
upper_white = np.array([359 , 0 , 100])
white_mask = cv2.inRange(hsv_frame ,lower_white,upper_white)
cv2.imshow('türkiye cennet cennet',frame)
cv2.imshow("masked white",white_mask)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',frame)
    cv2.destroyAllWindows()