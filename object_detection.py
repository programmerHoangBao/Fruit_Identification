import gradio as gr
from ultralytics import YOLO

# Load model YOLO đã được train (đảm bảo file best.pt nằm đúng đường dẫn)
model = YOLO("best.pt")

def detect_objects(image):
    """
    Hàm này nhận đầu vào là một ảnh (dạng numpy array),
    chạy model YOLO để detect đối tượng và trả về ảnh đã được vẽ bounding box.
    """
    # Chạy inference (sử dụng ngưỡng confidence 0.25, bạn có thể điều chỉnh)
    results = model.predict(source=image, conf=0.25)
    
    # Lấy ảnh đã được annotate từ kết quả của lần dự đoán đầu tiên
    annotated_image = results[0].plot()
    
    return annotated_image

# Tạo giao diện với Gradio
iface = gr.Interface(
    fn=detect_objects,                                  # Hàm xử lý
    inputs=gr.Image(type="numpy", label="Tải ảnh lên"),  # Input: Ảnh được tải lên
    outputs=gr.Image(type="numpy", label="Kết quả detect"),  # Output: Ảnh có bounding box
    title="Ứng dụng Phát hiện Trái cây",                 # Tiêu đề giao diện
    description="Tải ảnh lên để phát hiện các loại trái cây bằng mô hình YOLOv8"
)

# Chạy giao diện web
iface.launch()