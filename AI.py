
import mediapipe as mp 
from mediapipe.task import python
from mediapipe.task.python import vision 


cap = cv2.VideoCapture(0) # chọn cam máy  
cap.set(3,1080) # set độ rộng 
cap.set(4,1920) # set độ dài 
