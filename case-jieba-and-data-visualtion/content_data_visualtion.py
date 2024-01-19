import jieba, nltk, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import jieba.analyse
from nltk.corpus import stopwords
import pickle

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
nltk.data.path.append(path)
# nltk.download('stopwords',download_dir=path)
documents_path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/result_v1_text.txt'

with open(documents_path,'r',encoding='utf-8') as f:
    content = f.read()

print(content[0])

# with open(documents_path,'rb') as f:
#     loaded_data = pickle.load(f)

# print(f'loaded data {loaded_data}')    

"""
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(content)

pt.figure(figsize=(10, 5))
pt.imshow(wordcloud, interpolation='bilinear')
pt.axis('off')
pt.show()
"""
