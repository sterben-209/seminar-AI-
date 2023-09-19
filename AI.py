import mediapipe as mp 
import cv2 


cap = cv2.VideoCapture(0) # chọn cam máy  
cap.set(3,1080) # set độ rộng 
cap.set(4,1920) # set độ dài 
detector = HandDetector(detectionCon = 0.8)