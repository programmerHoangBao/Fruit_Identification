import cv2
import os

# Đường dẫn đến thư mục chứa ảnh
input_folder = "TraiCayScratch"
output_folder = "TraiCay640x640"

# Tạo thư mục đích nếu chưa có
os.makedirs(output_folder, exist_ok=True)

# Danh sách các thư mục con (các loại trái cây)
categories = ["SauRieng", "ThanhLong", "Tao"]

# Duyệt qua từng thư mục trái cây
for category in categories:
    input_path = os.path.join(input_folder, category)
    output_path = os.path.join(output_folder, category)
    os.makedirs(output_path, exist_ok=True)

    # Duyệt qua từng file ảnh trong thư mục
    for filename in os.listdir(input_path):
        img_path = os.path.join(input_path, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Lỗi đọc ảnh: {img_path}")
            continue

        # Resize ảnh về 640x640
        img_resized = cv2.resize(img, (640, 640))

        # Lưu ảnh đã resize
        cv2.imwrite(os.path.join(output_path, filename), img_resized)

print("Hoàn thành chuẩn hóa ảnh!")
