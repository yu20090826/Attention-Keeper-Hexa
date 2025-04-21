import cv2

# 開啟攝像頭（0 表示第一個攝像頭）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝像頭")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取畫面")
        break

    # 顯示畫面
    cv2.imshow('教室即時監控', frame)

    # 按下 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()
