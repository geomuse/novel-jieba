import jieba , nltk 
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import jieba.analyse
from nltk.corpus import stopwords

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
nltk.data.path.append(path)
nltk.download('stopwords',download_dir=path)
documents_path = '/home/geo/Downloads/geo/text_mining_bot/local_database/input_novel.md'

with open(documents_path,'r',encoding='utf-8') as f:
      markdown_content = f.read()

# content = str.split("。",markdown_content)
content = str(markdown_content).split("。")
# jieba.load_userdict('/home/geo/Downloads/geo/text_mining_bot/local_database/user_dict.txt')

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

# chinese_stopwords = set(stopwords.words('chinese'))

content = [split_text(sentence) for sentence in content]
content = [stop_punctuation(sentence) for sentence in content]
print(content)

with open("/home/geo/Downloads/geo/text_mining_bot/result_text.txt",'w',encoding='utf-8') as f :
      for _ in content :
            f.write(f'{str(_)}\n')

