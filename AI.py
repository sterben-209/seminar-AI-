import mediapipe as mp
import hand_detection_lib as handlib
import cv2
import math

x = 0.0
y = 0.0
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
                        for hand_landmarks in results.multi_hand_landmarks:
                            index_finger_landmark = hand_landmarks.landmark[8]
                            x, y = index_finger_landmark.x*1280, index_finger_landmark.y*720
                            cv2.circle(img, (x,y), 1, (255, 255, 255), 10)
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
            # Trích ra các toạ độ của khớp của các ngón tay
            firstHand = results.multi_hand_landmarks[0]
            h,w,_ = img.shape
            for hand_landmarks in results.multi_hand_landmarks:
                # Lấy vị trí của ngón trỏ
                index_finger_landmark = hand_landmarks.landmark[8]
                global x, y
                x, y = index_finger_landmark.x, index_finger_landmark.y
                
        return img, hand_lms
    









# Khởi tạo instance của lớp handDetector
detector = handDetector()

#khởi tạo camera
cap = cv2.VideoCapture(0)


while True :

    ret , frame = cap.read()
    frame = cv2.flip(frame,1)
    frame, hand_lms = detector.findHands(frame)
    #show màn hình quay được 
    frame = detector.draw(frame)
    canvas = cv2.Canvas(1280,720,cv2.CV_8UC3,(0,0,0))
    cv2.addWeighted(canvas,0.5,frame,0.5,0,frame) 
    cv2.imshow("MediaPipe Camera Preview", frame)




    #nút tắt chương trình 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
