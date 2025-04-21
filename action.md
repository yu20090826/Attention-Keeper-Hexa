#流程
打在終端機
sudo apt update
sudo apt install python3-opencv

將程式存成 camera_test.py，然後在 Jetson Nano 上執行：
python3 camera_test.py

你需要蒐集一些圖片，例如：

學生拿著手機的畫面

學生正常上課沒拿手機的畫面（也有幫助模型學會什麼「不是手機」）

數量建議：

至少 50～100 張手機畫面（越多越好）

每張照片都用 Bounding Box 標示手機的位置

上傳圖片

標註每張圖裡的手機（命名為 "phone" 或你想要的 label）

點「Generate Dataset」

選格式：YOLOv8 (Ultralytics)

點「Download Dataset」，拿到訓練資料的 zip 包

Colab 訓練模板 

點這個開始訓練：
https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/train_custom_data.ipynb

只要修改幾個地方：

把 roboflow 下載的 zip 上傳

設定 label 名稱（如 "phone"）

設定訓練參數（可保持預設）

訓練完後，會拿到一個 .pt 模型檔（如：best.pt）

 步驟 4：把模型拿到 Jetson Nano 上使用
你可以透過：

USB 傳輸

scp 指令（遠端複製）

或雲端硬碟下載

將 best.pt 放到 Jetson Nano，就可以接著寫 YOLOv8 + OpenCV 的即時偵測程式