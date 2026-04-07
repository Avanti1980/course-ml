from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
print(diabetes.DESCR)
# --------------------
# Ten baseline variables, age, sex, body mass index, average blood
# pressure, and six blood serum measurements were obtained for each of n =
# 442 diabetes patients, as well as the response of interest, a
# quantitative measure of disease progression one year after baseline.
# 
# **Data Set Characteristics:**
# 
# :Number of Instances: 442
# 
# :Number of Attributes: First 10 columns are numeric predictive values
# 
# :Target: Column 11 is a quantitative measure of disease progression one year # after baseline
# 
# :Attribute Information:
#     - age     年龄
#     - sex     性别
#     - bmi     身体质量指数
#     - bp      平均血压
#     - s1      血清总胆固醇
#     - s2      低密度脂蛋白
#     - s3      高密度脂蛋白
#     - s4      总胆固醇 / 高密度脂蛋白
#     - s5      血清甘油三酯水平的对数
#     - s6      血糖水平
# 
# Note: Each of these 10 feature variables have been mean centered and scaled by # the standard deviation times the square root of `n_samples` (i.e. the sum of # squares of each column totals 1).
# 
# Source URL:
# https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
# 
# For more information see:
# Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani (2004) # "Least Angle Regression," Annals of Statistics (with discussion), 407-499.
# (https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf)
