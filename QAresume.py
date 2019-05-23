import jieba
jieba.set_dictionary('dict.txt.big')
import requests
# import xgboost as xgb
import json
import numpy as np
from sklearn.externals import joblib

# 載入預測好的模型
svm_clf = joblib.load("train1_SVM_model.m")

with open('cat_mapping', 'r' , encoding='utf8') as f:
    cat_mapping = json.load(f)

with open('vectorterms', 'r' , encoding='utf8') as f:
    vectorterms = json.load(f)

# 模型預測
def predict_cat(test_sentence):
    words = list(jieba.cut(test_sentence, cut_all=False))

    self_main_list = [0] * len(vectorterms)
    for term in words:
        if term in vectorterms:
            idx = vectorterms.index(term)
            self_main_list[idx] += 1

    vector = self_main_list
    cat_num = svm_clf.predict(np.array([vector,]))[0]
    cat = None
    for key, value in cat_mapping.items():
        if str(int(cat_num)) == str(value):
            cat = key

    return cat
