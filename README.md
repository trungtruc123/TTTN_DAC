
# 1. RECOGNITION SKIN DESEASE DEMO IN WEB USE FLASK
# 2. RECOGNITION SKIN DESEASE DEMO IN APP USER FLUTTER
(github: https://github.com/trungtruc123/flutter_skin )
# 2. Giới thiệu đề tài
Bệnh ngoài da là loại bệnh rất phổ biến ở bất kỳ lứa tuổi nào. Tuy bệnh không nguy hiểm đến tính mạng nhưng ảnh hưởng trực tiếp đến bề mặt da gây mất thẩm mỹ, ảnh hưởng đến tâm lý của người bệnh gây mất tự tin trong giao tiếp và khó khăn trong việc sinh hoạt hằng ngày.
<img src ='/display/desease_skin.jpg'>
Ứng dụng chỉ cần bạn chụp 1 bức ảnh về vùng da có dấu hiệu bất thường, ứng dụng sẽ chuẩn đoán bệnh với độ chính xác khoảng 80% và đưa ra các lời khuyên , các điều trị hợp lí nhất.

* Hiện tại mới nhận diện được 7 bệnh về da : nv, mel, bkl, bcc, akiec, df, vasc
## 2.1. Mục đích:
Các bệnh về da rất phổ biến và dễ mắc phải, ảnh hưởng đến cuộc sống sinh hoạt của mọi người, muốn biết được bệnh thì phải đến bệnh viện hoặc cơ sở y tế để chuẩn đoán nhưng nhiều người thấy tự ti, và không có thời gian để đến bệnh viện. Trên cở sở đó em xây dựng 1 web , app chuẩn đoán các bệnh về da .Chỉ cần chụp ảnh vùng da có dấu hiệu bị bệnh thì sẽ đưa ra bệnh và các cách khắc phục , điều trị . Đề tài này mục đích nghiên cứu nên độ chính xác không cao.
## 2.2. Mục tiêu:
Nắm rõ được các kiến thức cơ bản về machine learning, deep learning.
Sử dụng được thành thạo framework Keras, Tensorflow
Nắm vững các mô hình của deep learning ( CNN,..)
Hoàn thành các nhiệm vụ được phân công đúng tiến độ
## 2.3. Thành viên
Trần Trung Trực -16T3
## 2.4. Data train, model:
* Data bộ dữ liệu HAM1000 datasets: https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000
* Liên hệ: fb: https://www.facebook.com/profile.php?id=100038801181933
# 3. Giao diện ứng dụng
** Giao diện home **
<img src ='/display/home.png'>
** Giao diện  upload **
<img src ='/display/upload.png'>
** Giao diện uploaded images **
<img src ='/display/uploaded_image.png'>
** Giao diện predict **
<img src ='/display/prediction.png'>

# 4. Môi trường cài đặt 
- **python3 **
- tensorflow 1.14
- flask
- pip install -r requirements.txt
- Ngoài ra còn 1 số thư viện có thể cài thêm trong quá trình chạy
# 5. Hướng dẫn chạy
- create envs skin : conda create -n skin python==3.6
- activate skin :   source activate skin
-
- open directory project and open terminal: git clone https://github.com/trungtruc123/TTTN_DAC
- pip install -r requirements.txt
- python3 app.py 
# 6. Hướng phát triển
Sau này có thể phát triển thành hệ thống web, app, nhận diện các bệnh về da, mắt, kết nối với các bác sĩ y tế để cho hướng dẫn kịp thời nhất.
# 7. Tài liệu tham khảo
https://arxiv.org/ftp/arxiv/papers/1907/1907.03220.pdf