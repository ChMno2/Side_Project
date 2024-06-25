import os

def convert_annotations(input_directory, output_directory, original_size, new_size):
    # 確保輸出目錄存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 遍歷輸入目錄中的所有檔案
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename)

            with open(input_file, 'r') as file:
                lines = file.readlines()

            converted_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue

                class_id = parts[0]
                x_center = float(parts[1]) * new_size / original_size
                y_center = float(parts[2]) * new_size / original_size
                width = float(parts[3]) * new_size / original_size
                height = float(parts[4]) * new_size / original_size

                converted_line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
                converted_lines.append(converted_line)

            with open(output_file, 'w') as file:
                file.writelines(converted_lines)

            print(f"檔案 {filename} 已成功轉換並儲存到 {output_file}")

# 設定輸入和輸出目錄
input_directory = r'C:\Users\chanmuen\Downloads\archive (2)\valid\labels'
output_directory = r'C:\Users\chanmuen\Downloads\archive (2)\valid\labels'
# 原始圖像大小
original_size = 416
# 新圖像大小
new_size = 640

# 轉換目錄中的所有標註檔
convert_annotations(input_directory, output_directory, original_size, new_size)
