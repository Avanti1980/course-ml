import numpy as np
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image

model = resnet50.ResNet50(weights='imagenet')
img = image.load_img('../img/tj/tj224x224.jpg', target_size=(224, 224))

# 增加通道数 RGB: (224, 224, 3) 灰度图: (224, 224, 1)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)  # batch_size = 1
x = resnet50.preprocess_input(x)  # 中心化

preds = model.predict(x)
print(resnet50.decode_predictions(preds, top=5)[0])

# ('n03630383', 'lab_coat', 0.24623604),     实验服
# ('n03877472', 'pajama', 0.17045474),       睡衣
# ('n04317175', 'stethoscope', 0.095500074), 听诊器
# ('n04479046', 'trench_coat', 0.07988542),  军用雨衣
# ('n03617480', 'kimono', 0.055965725),      和服