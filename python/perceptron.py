import numpy as np

X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])

y_and = np.array([1, -1, -1, -1])
y_or = np.array([1, 1, 1, 0])
y_not = np.array([0, 0, 1, 1])
y_xor = np.array([0, 1, 1, 0])

X_aug = np.hstack((X, - np.ones((4, 1))))

eta = 1

stop = 1

w = np.array([0, 0, 0])

# for i in range(len(X_aug)):
#     x, y = X_aug[i], y_and[i]
#     pre = w.dot(x) * y
#     if pre <= 0:
#         print(w, x)
#         w = w + eta *y * x

while stop < 20:
    stop = stop + 1
    for i in range(len(X_aug)):
        x, y = X_aug[i], y_and[i]
        pre = w.dot(x) * y
        if pre <= 0:
            print(stop, i, pre, w, x)
            w = w + eta * y * x
            # stop = 1

print(w)
