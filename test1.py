import cv2
import numpy as np
from tkinter import *

# Tạo canvas
canvas = np.zeros((1280, 720, 3), np.uint8)

# Tạo cửa sổ
window = Tk()
window.title("Python Paint")

# Tạo khung vẽ
canvas_frame = Frame(window)
canvas_frame.pack()

# Hiển thị canvas
canvas_image = cv2.imshow("Canvas", canvas)
canvas_image.pack()

# Vẽ lên canvas
def draw_on_canvas(event):
    # Lấy vị trí của con trỏ chuột
    x, y = event.x, event.y

    # Vẽ một điểm màu đỏ tại vị trí của con trỏ chuột
    cv2.circle(canvas, (x, y), 5, (0, 0, 255), -1)

    # Hiển thị canvas đã được cập nhật
    canvas_image.config(image=canvas)

# Gắn sự kiện vẽ lên khung vẽ
canvas_frame.bind("<B1-Motion>", draw_on_canvas)

# Lưu canvas
def save_canvas():
    # Lưu canvas thành một tệp hình ảnh
    cv2.imwrite("canvas.png", canvas)

# Tạo nút lưu
save_button = Button(window, text="Save", command=save_canvas)
save_button.pack()

# Khởi động vòng lặp chính của chương trình
window.mainloop()
