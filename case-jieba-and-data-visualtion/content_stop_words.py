import jieba, nltk, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import jieba.analyse
from nltk.corpus import stopwords
import pickle

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
nltk.data.path.append(path)
nltk.download('stopwords',download_dir=path)
documents_path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/input_novel.md'
stop_words_path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/stop_words.txt'

with open(documents_path,'r',encoding='utf-8') as f:
    markdown_content = f.read()

with open(stop_words_path,'r',encoding='utf-8') as f:
    stops = f.read()

content = str(markdown_content).split("。")

"""
[x] stop words
[x] punctuation
[ ] 
[ ] plot bubble
"""

"""
# for sentence in content :
#     seg_list = jieba.lcut(sentence)
#     print('|'.join(seg_list))
"""

def split_text(sentence):
    seg_list = jieba.lcut(sentence)
    # "|".join(seg_list)
    return seg_list

def stop_punctuation(sentence):
    sentence = str(sentence).replace('\\n','')
    sentence = sentence.replace('\\u3000','')
    return sentence

def remove_chinese_stopwords(text):
    words = jieba.lcut(text)
    filtered_words = [word for word in words if word not in stops]
    return ' '.join(filtered_words)

def find_chinese(content):
    pattern = re.compile('[\u4e00-\u9fff]+')
    result = re.findall(pattern, content)
    return result

content = [split_text(sentence) for sentence in content]
content = [stop_punctuation(sentence) for sentence in content]
content = [remove_chinese_stopwords(text=sentence) for sentence in content]
content = [find_chinese(sentence) for sentence in content] 

path = "/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/result_v1_text.txt"
with open(path,'w',encoding='utf-8') as f :
    for _ in content:
        f.write(f'{str(_)}\n')

contents = []
for _ in content:
    contents += _

path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/content.pickle'
with open(path,'wb') as f:
    pickle.dump(contents,f)

print(f'data saved to {path}')