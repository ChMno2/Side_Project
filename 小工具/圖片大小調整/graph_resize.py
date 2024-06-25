import os
from PIL import Image

def resize_images(input_directory, output_directory, size=(640, 640)):
    # 如果輸出目錄不存在，則創建它
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 遍歷輸入目錄中的所有檔案
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # 確保是圖片檔案
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 打開圖片
            image = Image.open(input_path)
            
            # 調整大小到指定的尺寸
            resized_image = image.resize(size)

            # 構建輸出路徑
            output_path = os.path.join(output_directory, filename)

            # 儲存調整後的圖片
            resized_image.save(output_path)

            print(f"圖片 {filename} 已成功放大並儲存到 {output_path}")

# 設定輸入和輸出目錄
input_directory = r'C:\Users\chanmuen\Downloads\archive (2)\valid\images'
output_directory = r'C:\Users\chanmuen\Downloads\archive (2)\valid\images'

# 調整目錄中的所有圖片大小
resize_images(input_directory, output_directory)
