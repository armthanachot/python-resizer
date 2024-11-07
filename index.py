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
resize_image("/Users/thanachottesjaroen/Downloads/_a3becdda-c6bc-4c49-896b-d4cef72ebcae-removebg-preview.png","img/8_.png", new_size)