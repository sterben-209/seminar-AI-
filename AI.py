import mediapipe as mp
import cv2
import math
import PIL.Image
from PIL import ImageDraw
import os 

x = 0
y = 0
list8 = [] 
list12 = []
do = (255,0,0)
xanhla = (0,255,0)
xanhduong = (0,0,255)
den = (0,0,0)
current_color=do 
mau = []





class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils


    def draw(self, frame,canvas,current_color ):
        i = 0  
        while True:          
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            if results.multi_hand_landmarks:
                # print("có tay") 
                for hand_landmarks in results.multi_hand_landmarks:
                    toa_do_dau_ngon_tro = hand_landmarks.landmark[8]
                    toa_do_dau_ngon_giua = hand_landmarks.landmark[12]
                    x8, y8 = toa_do_dau_ngon_tro.x*1280, toa_do_dau_ngon_tro.y*720
                    x12, y12 = toa_do_dau_ngon_giua.x*1280, toa_do_dau_ngon_giua.y*720

                    cv2.circle(frame, (math.ceil(x8),math.ceil(y8)), 5,current_color, 10)    
                    list8.append((math.ceil(x8),math.ceil(y8)))
                    list12.append((math.ceil(x12),math.ceil(y12)))
                    i += 1 
                    mau.append(current_color)
                    if len(list8) > 1 :
                        print(current_color)
                        for i  in range(1 , len(list8)) :
                            if list12[i][1] >= list8[i][1]:                                
                                draw.line((list8[i-1][0],list8[i-1][1],list8[i][0],list8[i][1]),fill = (mau[i][2],mau[i][1],mau[i][0]))     
                            elif 0 <= x12 and x12 <= 320 and y12 <= 30 :
                                current_color = do
                                mau.append(current_color)
                                print(do)
                            elif 321 <= x12 and x12 <= 640 and y12 <= 30 :
                                current_color = xanhla
                                mau.append(current_color)
                            elif 641 <= x12 and x12 <= 960 and y12 <= 30 :
                                current_color = xanhduong
                                mau.append(current_color)
                            elif 961 <= x12 <= 1280 and 0 <= y12 <= 30 :
                                current_color = den                 
                            # print(x12,y12)     
                        list8.pop(0)
                        list12.pop(0)
                        # mau.pop(0)
                    canvas.save("canva.png")

            return canvas


    
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



# Khởi tạo instance của lớp handDetector
detector = handDetector()

#khởi tạo camera
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# dùng pil tạo canvas 
canvas = PIL.Image.open("canva.png")


global draw
draw = ImageDraw.Draw(canvas)

draw.rectangle((0, 0, 1280, 720), fill=(0, 0, 0))
canvas.save("canva.png")

while True :
    
    os.environ['MEDIAPIPE_GPU'] = '1'

    ret , frame = cap.read()
    frame = cv2.flip(frame,1)

    detector.hands = detector.mpHands.Hands(max_num_hands=1)


    frame, hand_lms = detector.findHands(frame)   


    
    canvas = detector.draw(frame,canvas,current_color)
    canva = cv2.imread("canva.png")
    # detector.color_pic(frame)
    cv2.rectangle(frame,(0,0),(320,30),do,-1)
    cv2.rectangle(frame,(321,0),(640,30),xanhla,-1)
    cv2.rectangle(frame,(641,0),(960,30),xanhduong,-1)
    cv2.rectangle(frame,(961,0),(1280,30),den,-1)

    frame = cv2.addWeighted(canva,1,frame,1,0)
    cv2.imshow("frame", frame)
    # cv2.imshow("canva", canva)
    


    #nút tắt chương trình 
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
