import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD, Adam

X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([0, 1, 1, 0])

model = Sequential()
model.add(Dense(3, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(optimizer=Adam(0.01),
              loss="binary_crossentropy",
              metrics=["accuracy"],
              )

model.fit(X, y, epochs=10)
model.evaluate(X, y, verbose=2)
