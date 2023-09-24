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
            global counttt 
            counttt = 0
            global counttp
            counttp = 0
            count = 0
            def hamcounttp():
                # counttp = 0;
                imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(imgRGB)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        toa_do_dau_ngon_tro = hand_landmarks.landmark[8]
                        toa_do_giua_ngon_tro = hand_landmarks.landmark[7]
                        y8,y7 = toa_do_dau_ngon_tro.y*720, toa_do_giua_ngon_tro.y*720
                        if y7 > y8 : nttp = 1
                        else : nttp = 0
                        toa_do_dau_ngon_giua = hand_landmarks.landmark[12]
                        toa_do_giua_ngon_giua = hand_landmarks.landmark[11]
                        y12,y11 = toa_do_dau_ngon_giua.y*720, toa_do_giua_ngon_giua.y*720
                        if y11 > y12 : ngtp = 1
                        else : ngtp = 0
                        toa_do_dau_ngon_cai = hand_landmarks.landmark[4]
                        toa_do_giua_ngon_cai = hand_landmarks.landmark[1]
                        x4,x1 = toa_do_dau_ngon_cai.x*1280, toa_do_giua_ngon_cai.x*1280
                        if x4 < x1 : nctp = 1
                        else : nctp = 0
                        toa_do_dau_ngon_aput = hand_landmarks.landmark[16]
                        toa_do_giua_ngon_aput = hand_landmarks.landmark[15]
                        y16,y15 = toa_do_dau_ngon_aput.y*720, toa_do_giua_ngon_aput.y*720
                        if y15 > y16 : nautp = 1
                        else : nautp = 0
                        toa_do_dau_ngon_ut = hand_landmarks.landmark[20]
                        toa_do_giua_ngon_ut = hand_landmarks.landmark[19]
                        y20,y19 = toa_do_dau_ngon_ut.y*720, toa_do_giua_ngon_ut.y*720
                        if y19 > y20 : nutp = 1 
                        else: nutp = 0
                    counttp = nctp + nttp + ngtp + nautp + nutp 
                    print(counttp)
                    return counttp

                
            def hamcounttt() :
                # counttt = 0
                imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(imgRGB)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        toa_do_dau_ngon_tro = hand_landmarks.landmark[8]
                        toa_do_giua_ngon_tro = hand_landmarks.landmark[7]
                        y8,y7 = toa_do_dau_ngon_tro.y*720, toa_do_giua_ngon_tro.y*720
                        if y7 > y8 : nttt = 1
                        else : nttt = 0
                        toa_do_dau_ngon_giua = hand_landmarks.landmark[12]
                        toa_do_giua_ngon_giua = hand_landmarks.landmark[11]
                        y12,y11 = toa_do_dau_ngon_giua.y*720, toa_do_giua_ngon_giua.y*720
                        if y11 > y12 : ngtt = 1
                        else : ngtt = 0
                        toa_do_dau_ngon_cai = hand_landmarks.landmark[4]
                        toa_do_giua_ngon_cai = hand_landmarks.landmark[1]
                        x4,x1 = toa_do_dau_ngon_cai.x*1280, toa_do_giua_ngon_cai.x*1280
                        if x4 > x1 : nctt = 1
                        else : nctt = 0
                        toa_do_dau_ngon_aput = hand_landmarks.landmark[16]
                        toa_do_giua_ngon_aput = hand_landmarks.landmark[15]
                        y16,y15 = toa_do_dau_ngon_aput.y*720, toa_do_giua_ngon_aput.y*720
                        if y15 > y16 : nautt = 1
                        else : nautt = 0
                        toa_do_dau_ngon_ut = hand_landmarks.landmark[20]
                        toa_do_giua_ngon_ut = hand_landmarks.landmark[19]
                        y20,y19 = toa_do_dau_ngon_ut.y*720, toa_do_giua_ngon_ut.y*720
                        if y19 > y20 : nutt = 1 
                        else: nutt = 0
                    counttt = nctt + nttt + ngtt + nautt + nutt
                    print(counttt)
                    return counttt

                   
                count = counttt + counttp
            cv2.putText(frame,str(counttp),(640,150),cv2.FONT_ITALIC,3,(0,255,0),10)
            return frame




detector = handDetector()

cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)

while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)

    
    frame, hand_lms = detector.findHands(frame)   
    detector.count(frame)
    cv2.imshow("fingers count",frame )    
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows
