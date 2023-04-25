import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

document1 = "I have a pen, I have an apple, apple pen."
document2 = "I have a pen, I have pineapple, pineapple pen."

tv = TfidfVectorizer(lowercase=False, token_pattern='\w+',
                     norm='l1', smooth_idf=False)
model = tv.fit_transform([document1, document2])
print(pd.DataFrame(model.toarray(), columns=tv.get_feature_names_out()))
#           I         a        an     apple      have       pen  pineapple
# 0  0.165571  0.082785  0.140168  0.280335  0.165571  0.165571   0.000000
# 1  0.192561  0.096281  0.000000  0.000000  0.192561  0.192561   0.326035
