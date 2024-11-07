from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    # เปิดภาพต้นฉบับ
    with Image.open(input_image_path) as img:
        # ปรับขนาดภาพโดยใช้ LANCZOS filter เพื่อรักษาความคมชัด
        resized_image = img.resize(size, Image.LANCZOS)
        # บันทึกภาพที่ถูกปรับขนาดลงไปยังไฟล์ใหม่
        resized_image.save(output_image_path)

# ขนาดที่ต้องการปรับ (กว้าง, สูง)
new_size = (60, 60)

# เรียกใช้ฟังก์ชัน resize
resize_image("source/image/image.png","img/8_.png", new_size)