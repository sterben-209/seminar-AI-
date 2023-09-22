import mediapipe as mp
import numpy as np
import cv2
import math

x = 0
y = 0
listx = [] 
listy = [] 
current_color = (0,0,0)





class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils


    def draw(self, img):
        while True:
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            if results.multi_hand_landmarks:
                print("có tay")
                while cv2.waitKey(1) == ord("d"):
                        print("có nhấn d ")
                        for hand_landmarks in results.multi_hand_landmarks:
                            index_finger_landmark = hand_landmarks.landmark[8]
                            x, y = index_finger_landmark.x, index_finger_landmark.y
                            cv2.circle(img, (150,1500), 1, (255, 255, 255), 1000)
                            cv2.line(img,(0,0),(0,0),(255,0,0),10)
                            print(x,y)
            return frame

    def findHands(self, img):
        # Chuyển từ BGR thành RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Đưa vào thư viện mediapipe
        results = self.hands.process(imgRGB)
        hand_lms = []
        

        if results.multi_hand_landmarks:
            # Vẽ landmark cho các bàn tay      
            for handlm in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handlm, self.mpHands.HAND_CONNECTIONS)
        return img, hand_lms
    
    def color_pic(self):
        
        do = (255,0,0)
        xanhla = (0,255,0)
        xanhduong = (0,0,255)
        den = (255,255,255)

        cv2.rectangle(canvas,(0,0),(320,10),do,10)
        cv2.rectangle(canvas,(321,0),(640,10),xanhla,10)
        cv2.rectangle(canvas,(641,0),(960,10),xanhduong,10)
        cv2.rectangle(canvas,(961,0),(1280,10),den,10)



# Khởi tạo instance của lớp handDetector
detector = handDetector()

#khởi tạo camera
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


while True :

    ret , frame = cap.read()
    frame = cv2.flip(frame,1)
    frame, hand_lms = detector.findHands(frame)
    #show màn hình quay được 
    frame = detector.draw(frame)

    cv2.imshow("MediaPipe Camera Preview", frame)




    #nút tắt chương trình 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
