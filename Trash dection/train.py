import os
import shutil
import time
from ultralytics import YOLO

if __name__=='__main__':
    train_path="./runs/2"
    if os.path.exists(train_path):
        shutil.rmtree(train_path)
    model = YOLO("yolov8n.pt")
    print("開始訓練 .........")
    t1=time.time()
    model.train(data="./data.yaml", epochs=10, imgsz=640, batch=8, 
                close_mosaic=0, lr0=0.005, optimizer='Adam', cos_lr=True)
    t2=time.time()
    print(f'訓練花費時間 : {t2-t1}秒')#2131.11984705925秒, epochs : 121
    path=model.export()
    print(f'模型匯出路徑 : {path}')