from sklearn.metrics import accuracy_score

y_true = [0, 1, 2, 3]
y_pred = [0, 2, 1, 3]

print(accuracy_score(y_true, y_pred))  # 百分比
# 0.5

print(accuracy_score(y_true, y_pred, normalize=False))  # 正确分类的个数
# 2
