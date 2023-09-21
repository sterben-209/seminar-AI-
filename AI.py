
import mediapipe as mp
import hand_detection_lib as handlib
import os
import cv2



def __init__(self):
    self.mpHands = mp.solutions.hands
    self.hands = self.mpHands.Hands()
    self.mpDraw = mp.solutions.drawing_utils

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
            x, y = index_finger_landmark.x, index_finger_landmark.y
            print(x,y)
    return img, hand_lms,x ,y
    
def draw(x,y):
    while True:
        print(x,y)


#khởi tạo camera
cap = cv2.VideoCapture(0)


while True :
    ret , frame = cap.read()
    Flippedframe = cv2.flip(frame,1)
    frame, hand_lms, x, y = findHands(,Flippedframe)
    draw(x,y)
    #show màn hình quay được 
    cv2.imshow("MediaPipe Camera Preview", Flippedframe)
    # draw()
    # nút bắt đầu vẽ 
    # if cv2.waitKey(1) == ord("d"):


    #nút tắt chương trình 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


