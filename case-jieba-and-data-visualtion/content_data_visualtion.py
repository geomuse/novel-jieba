import jieba, nltk, re
import numpy as np
import pandas as pd

import matplotlib.pyplot as pt
from matplotlib import style
style.use('ggplot')

from nltk.corpus import stopwords
import pickle

import matplotlib.pyplot as pt
from matplotlib import font_manager
from collections import Counter

import warnings
warnings.filterwarnings("ignore")

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
nltk.data.path.append(path)
# nltk.download('stopwords',download_dir=path)

file_path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/content.pickle'

with open(file_path, 'rb') as file:
    content = pickle.load(file)

# print('loaded list:', content)
# fontP = font_manager.FontProperties()
# fontP.set_family('SimHei')
# fontP.set_size(11)

word_counts = Counter(content)
words = list(word_counts.keys())
counts = list(word_counts.values())

df = pd.DataFrame({'words': words , 'counts': counts})
df = df.sort_values(by='counts',ascending=False)

pt.bar(df['words'], df['counts'],alpha=0.6)
pt.plot(df['words'], df['counts'],"x-",color='blue',alpha=0.6)
pt.xlabel('text')
pt.ylabel('frequency')
pt.title('distribution?')
pt.show()