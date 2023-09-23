import mediapipe as mp 
import cv2 

class handDetector():
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
        return img, hand_lms
    def count(self,frame):
        while True:
            count = 0;
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    toa_do_dau_ngon_tro = hand_landmarks.landmark[8]
                    toa_do_giua_ngon_tro = hand_landmarks.landmark[7]
                    y8,y7 = toa_do_dau_ngon_tro.y*720, toa_do_giua_ngon_tro.y*720
                    if y7 > y8 :count += 1 
                    toa_do_dau_ngon_giua = hand_landmarks.landmark[12]
                    toa_do_giua_ngon_giua = hand_landmarks.landmark[11]
                    y12,y11 = toa_do_dau_ngon_giua.y*720, toa_do_giua_ngon_giua.y*720
                    if y11 > y12 :count += 1 
                    toa_do_dau_ngon_cai = hand_landmarks.landmark[4]
                    toa_do_giua_ngon_cai = hand_landmarks.landmark[3]
                    y4,y3 = toa_do_dau_ngon_cai.y*720, toa_do_giua_ngon_cai.y*720
                    if y3 > y4 :count += 1 
                    toa_do_dau_ngon_aput = hand_landmarks.landmark[16]
                    toa_do_giua_ngon_aput = hand_landmarks.landmark[15]
                    y16,y15 = toa_do_dau_ngon_aput.y*720, toa_do_giua_ngon_aput.y*720
                    if y15 > y16 :count += 1 
                    toa_do_dau_ngon_ut = hand_landmarks.landmark[20]
                    toa_do_giua_ngon_ut = hand_landmarks.landmark[19]
                    y20,y19 = toa_do_dau_ngon_ut.y*720, toa_do_giua_ngon_ut.y*720
                    if y19 > y20 : count += 1 
        return count  




detector = handDetector()

cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)

while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)

    
    detector.hands = detector.mpHands.Hands(max_num_hands=1)
    frame, hand_lms = detector.findHands(frame)   
    # detector.count(frame)
    # cv2.addText(frame,detector.count(frame),(0,0),pointSize=20)
    # cv2.imshow("fingers count",frame )    
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows