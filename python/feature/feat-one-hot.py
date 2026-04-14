import numpy as np
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder

X = np.array([
    [1, '周六', '吃饭', '晴天', '轻松', '清零', '精彩'],
    [6, '周六', '逛街', '晴天', '轻松', '平缓', '无聊'],
    [10, '周六', '-', '雨天', '轻松', '严峻', '无聊'],
    [13, '周六', '逛街', '晴天', '正常', '清零', '精彩'],
])
y = np.array(['是', '是', '否', '否'])
print(LabelBinarizer().fit_transform(y).squeeze())  # 标记二值化
# [1 1 0 0]

enc = OneHotEncoder()
print(enc.fit_transform(X[:, 1:7]).toarray())  # 对6个类别特征采用独热编码
# [[1. 0. 1. 0. 1. 0. 0. 1. 0. 0. 1. 0. 1.]
#  [1. 0. 0. 1. 1. 0. 0. 1. 0. 1. 0. 1. 0.]
#  [1. 1. 0. 0. 0. 1. 0. 1. 1. 0. 0. 1. 0.]
#  [1. 0. 0. 1. 1. 0. 1. 0. 0. 0. 1. 0. 1.]]

print(enc.get_feature_names_out())  # 独热编码对应的原始特征
# ['x0_周六' 'x1_-' 'x1_吃饭' 'x1_逛街' 'x2_晴天' 'x2_雨天' 'x3_正常' 'x3_轻松' 'x4_严峻'
#  'x4_平缓' 'x4_清零' 'x5_无聊' 'x5_精彩']
