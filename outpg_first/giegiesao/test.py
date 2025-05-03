import cv2
import numpy as np
from rembg import remove
from PIL import Image
from io import BytesIO
import os

# 输出文件夹
OUTPUT_DIR = "test_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def remove_background(input_path, output_name="removed_bg.png"):
    with open(input_path, "rb") as f:
        image_data = f.read()
        result = remove(image_data)
    output_path = os.path.join(OUTPUT_DIR, output_name)
    with open(output_path, "wb") as f:
        f.write(result)
    print(f"[✔] 背景去除完成：{output_path}")

def resize_image(input_path, width=300, height=300, output_name="resized.png"):
    image = cv2.imread(input_path)
    resized = cv2.resize(image, (width, height))
    output_path = os.path.join(OUTPUT_DIR, output_name)
    cv2.imwrite(output_path, resized)
    print(f"[✔] 大小调整完成：{output_path}")

def crop_image(input_path, x=0, y=0, w=100, h=100, output_name="cropped.png"):
    image = cv2.imread(input_path)
    cropped = image[y:y+h, x:x+w]
    output_path = os.path.join(OUTPUT_DIR, output_name)
    cv2.imwrite(output_path, cropped)
    print(f"[✔] 裁剪完成：{output_path}")

def enhance_contrast(input_path, output_name="enhanced_contrast.png"):
    image = cv2.imread(input_path)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    enhanced = cv2.merge([l, a, b])
    result = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
    output_path = os.path.join(OUTPUT_DIR, output_name)
    cv2.imwrite(output_path, result)
    print(f"[✔] 对比度增强完成：{output_path}")

# 示例测试用例（替换为你自己的文件路径）
if __name__ == "__main__":
    input_file = "test.png"  # 你要测试的图片路径

    remove_background(input_file)
    #resize_image(input_file, width=400, height=400)
    #crop_image(input_file, x=50, y=50, w=200, h=200)
    #enhance_contrast(input_file)
