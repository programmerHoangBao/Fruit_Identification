import os
import shutil
import random

# Đường dẫn gốc
image_dir = os.path.join("TraiCay640x640")
label_dir = os.path.join("TraiCayYoLo")
dataset_dir = os.path.join("dataset")

# Tạo thư mục dataset theo cấu trúc YOLO
for sub in ["images/train", "images/val", "labels/train", "labels/val"]:
    os.makedirs(os.path.join(dataset_dir, sub), exist_ok=True)

# Danh sách loại trái cây
fruit_types = ["SauRieng", "Tao", "ThanhLong"]

# Chia tập train và val (80% - 20%)
for fruit in fruit_types:
    img_path = os.path.join(image_dir, fruit)
    lbl_path = os.path.join(label_dir, fruit)
    
    images = [f for f in os.listdir(img_path) if f.endswith(".jpg") or f.endswith(".png")]
    random.shuffle(images)
    
    train_size = int(0.8 * len(images))
    train_images = images[:train_size]
    val_images = images[train_size:]
    
    # Copy train images and labels
    for img in train_images:
        shutil.copy(os.path.join(img_path, img), os.path.join(dataset_dir, "images/train", img))
        label_file = os.path.splitext(img)[0] + ".txt"
        if os.path.exists(os.path.join(lbl_path, label_file)):
            shutil.copy(os.path.join(lbl_path, label_file), os.path.join(dataset_dir, "labels/train", label_file))
    
    # Copy val images and labels
    for img in val_images:
        shutil.copy(os.path.join(img_path, img), os.path.join(dataset_dir, "images/val", img))
        label_file = os.path.splitext(img)[0] + ".txt"
        if os.path.exists(os.path.join(lbl_path, label_file)):
            shutil.copy(os.path.join(lbl_path, label_file), os.path.join(dataset_dir, "labels/val", label_file))

print("Dữ liệu đã được tổ chức thành công theo chuẩn YOLOv!")
