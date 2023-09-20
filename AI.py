
import mediapipe as mp
import hand_detection_lib as handlib
import os
import cv2

detector = handlib.handDetector()
#khởi tạo camera
cap = cv2.VideoCapture(0)



while True :
    ret , frame = cap.read()
    Flippedframe = cv2.flip(frame,1)
    frame, hand_lms = detector.findHands(Flippedframe)
    #show màn hình quay được 
    cv2.imshow("MediaPipe Camera Preview", Flippedframe)
        
    #nút tắt chương trình 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


