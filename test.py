import mediapipe as mp
import cv2

# Khởi tạo pipeline object detection
object_detection = mp.solutions.object_detection.ObjectDetection(
    model_path="models/object_detection/mobilenet_ssd_v2_coco.tflite"
)

# Đọc video
cap = cv2.VideoCapture("video.mp4")

while True:
    # Đọc khung hiện tại từ video
    ret, frame = cap.read()

    # Nếu không có khung, thoát vòng
    if not ret:
        break

    # Chạy pipeline trên khung
    results = object_detection.process(frame)

    # Vẽ kết quả trên khung
    for detection in results.detections:
        cv2.rectangle(frame, detection.bounding_box, (255, 0, 0), 2)
        cv2.putText(frame, detection.label, detection.bounding_box.center, cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

    # Hiển thị khung
    cv2.imshow("Output", frame)

    # Kiểm tra phím ESC để thoát
    key = cv2.waitKey(1)
    if key == 27:
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
