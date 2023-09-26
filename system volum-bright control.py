import mediapipe as mp 
import cv2
# import pycaw
# from ctypes import POINTER, cast
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math 
# from comtypes import CLSCTX_ALL
import pyautogui


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

    def hand_check(self):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                toa_do_dau_ngon_cai = hand_landmarks.landmark[4]
                x4,y4 = toa_do_dau_ngon_cai.x*1280, toa_do_dau_ngon_cai.y*720
                toa_do_giua_ngon_cai = hand_landmarks.landmark[3]
                x3,y3 = toa_do_giua_ngon_cai.x*1280,toa_do_giua_ngon_cai.y*720
                toa_do_dau_ngon_tro = hand_landmarks.landmark[8]
                x8,y8 = toa_do_dau_ngon_tro.x*1280, toa_do_dau_ngon_tro.y*720
                toa_do_giua_ngon_tro = hand_landmarks.landmark[7]
                x7,y7 =  toa_do_giua_ngon_tro.x*1280,toa_do_giua_ngon_tro.y*720
                toa_do_dau_ngon_giua = hand_landmarks.landmark[12]
                x12,y12 = toa_do_dau_ngon_giua.x*1280,toa_do_dau_ngon_giua.y*720
                if x4 < x3 : nc = True 
                else: nc = False 
                if y8 < y7 : nt = True
                else: nt = False
                if  nc and nt : 
                    amount = math.sqrt(pow(x8-x4,2)+pow(y8-y4,2))
                    # pycaw.AudioUtilities.SetMasterVolume(amount, None)
                    if amount > 100 :
                        pyautogui.press("volumeup")
                    else:
                        pyautogui.press("volumedown")










cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
detector = handDetector()
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))


while True:
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)
    detector.findHands(frame)
    detector.hand_check()
    cv2.imshow("system volum-bringt control",frame) 
    if cv2.waitKey(1) == ord('q') :
        break
cam.release
cv2.destroyAllWindows