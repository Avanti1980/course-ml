import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.layers import (Conv2D, Dense, Dropout,
                                     Flatten, AveragePooling2D)
from tensorflow.keras.optimizers import Adam

(x_train, y_train), (x_test, y_test) = load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

model = Sequential()
model.add(Conv2D(6, (5, 5), activation="relu",
                 padding="same", input_shape=(28, 28, 1)))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Conv2D(16, (5, 5), activation="relu"))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Conv2D(120, (5, 5), activation="relu"))
model.add(Flatten())
model.add(Dense(84, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.summary()
# Model: "sequential"
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #   
# =================================================================
#  conv2d (Conv2D)             (None, 28, 28, 6)         156       
#                                                                  
#  average_pooling2d (AverageP  (None, 14, 14, 6)        0         
#  ooling2D)                                                       
#                                                                  
#  conv2d_1 (Conv2D)           (None, 10, 10, 16)        2416      
#                                                                  
#  average_pooling2d_1 (Averag  (None, 5, 5, 16)         0         
#  ePooling2D)                                                     
#                                                                  
#  conv2d_2 (Conv2D)           (None, 1, 1, 120)         48120     
#                                                                  
#  flatten (Flatten)           (None, 120)               0         
#                                                                  
#  dense (Dense)               (None, 84)                10164     
#                                                                  
#  dense_1 (Dense)             (None, 10)                850       
#                                                                  
# =================================================================
# Total params: 61,706
# Trainable params: 61,706
# Non-trainable params: 0

model.compile(
    optimizer=Adam(0.001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=5, verbose=1)
# Epoch 1/5
# 1875/1875 [==============================] - 7s 2ms/step - loss: 0.2085 - accuracy: 0.9356 
# Epoch 2/5
# 1875/1875 [==============================] - 4s 2ms/step - loss: 0.0657 - accuracy: 0.9795
# Epoch 3/5
# 1875/1875 [==============================] - 4s 2ms/step - loss: 0.0479 - accuracy: 0.9844
# Epoch 4/5
# 1875/1875 [==============================] - 4s 2ms/step - loss: 0.0372 - accuracy: 0.9886
# Epoch 5/5
# 1875/1875 [==============================] - 4s 2ms/step - loss: 0.0300 - accuracy: 0.9907

model.evaluate(x_test, y_test, verbose=2)
# 313/313 - 1s - loss: 0.0409 - accuracy: 0.9860 - 536ms/epoch - 2ms/step
