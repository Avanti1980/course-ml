from sklearn.metrics import (confusion_matrix, f1_score, precision_score,
                             recall_score)

y_true = [1, 1, 0, 0, 1, 0, 1, 0]
y_pred = [0, 1, 0, 1, 1, 1, 1, 0]

cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
print(cm)
# [[3 1]
#  [2 2]]

tp, fn, fp, tn = cm.ravel()
print(tp, fn, fp, tn)
# 3 1 2 2

print(precision_score(y_true, y_pred))
# 0.6

print(recall_score(y_true, y_pred))
# 0.75

print(f1_score(y_true, y_pred))
# 0.6666666666666665
