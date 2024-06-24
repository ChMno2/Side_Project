import os
import cv2

# 定义路径
image_folder = r'C:\Users\chanmuen\Downloads\archive (2)\train\images'  # 替换为你的图像文件夹路径
label_folder = r'C:\Users\chanmuen\Downloads\archive (2)\train\labels'  # 替换为你的标签文件夹路径
output_image_folder = 'path/to/output/images'  # 替换为输出图像文件夹路径
output_label_folder = 'path/to/output/labels'  # 替换为输出标签文件夹路径

# 确保输出文件夹存在
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# 目标图像尺寸
target_width = 640
target_height = 640

# 遍历图像文件夹
for image_filename in os.listdir(image_folder):
    if image_filename.endswith('.jpg') or image_filename.endswith('.png'):
        # 读取图像
        image_path = os.path.join(image_folder, image_filename)
        image = cv2.imread(image_path)
        original_height, original_width = image.shape[:2]

        # 调整图像尺寸
        resized_image = cv2.resize(image, (target_width, target_height))
        
        # 保存调整后的图像
        output_image_path = os.path.join(output_image_folder, image_filename)
        cv2.imwrite(output_image_path, resized_image)
        
        # 处理对应的标签文件
        label_filename = os.path.splitext(image_filename)[0] + '.txt'
        label_path = os.path.join(label_folder, label_filename)
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            output_label_path = os.path.join(output_label_folder, label_filename)
            with open(output_label_path, 'w') as f:
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_id = parts[0]
                        x_center = float(parts[1])
                        y_center = float(parts[2])
                        width = float(parts[3])
                        height = float(parts[4])
                        
                        # 调整标注框坐标
                        x_center = (x_center * original_width) / target_width
                        y_center = (y_center * original_height) / target_height
                        width = (width * original_width) / target_width
                        height = (height * original_height) / target_height
                        
                        # 写入新的标注文件
                        f.write(f'{class_id} {x_center} {y_center} {width} {height}\n')
