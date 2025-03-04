from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt

breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

lr = LogisticRegression().fit(X, y)
nb = GaussianNB().fit(X, y)

plt.figure(figsize=(8, 6))

y_scores = lr.predict_proba(X)[:, 1]
precision, recall, thresholds = precision_recall_curve(y, y_scores)
auc_score = auc(recall, precision)

plt.plot(recall, precision, label=f'Precision-Recall Curve (AUC = {auc_score:.2f})')

y_scores = nb.predict_proba(X)[:, 1]
precision, recall, thresholds = precision_recall_curve(y, y_scores)
auc_score = auc(recall, precision)

plt.plot(recall, precision, label=f'Precision-Recall Curve (AUC = {auc_score:.2f})')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()

print(X[0:3, :], y[0:3])
