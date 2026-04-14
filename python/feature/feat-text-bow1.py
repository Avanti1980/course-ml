import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

document1 = "I have a pen, I have an apple, apple pen."
document2 = "I have a pen, I have pineapple, pineapple pen."

cv = CountVectorizer(lowercase=False, token_pattern='\w+', binary=True)
model = cv.fit_transform([document1, document2])
print(pd.DataFrame(model.toarray(), columns=cv.get_feature_names_out()))
#    I  a  an  apple  have  pen  pineapple
# 0  1  1   1      1     1    1          0
# 1  1  1   0      0     1    1          1
