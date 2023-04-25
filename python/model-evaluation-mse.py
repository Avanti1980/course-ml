from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print(mean_squared_error(y_true, y_pred))  # 均方误差
# 0.375

print(mean_squared_error(y_true, y_pred, squared=False))  # 均方根误差
# 0.6123724356957945
