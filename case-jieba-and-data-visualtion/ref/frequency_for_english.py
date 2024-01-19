import pandas as pd
import matplotlib.pyplot as pt
from matplotlib import style
style.use('ggplot')

# 假设你有一个包含列 'Keyword' 和 'Frequency' 的 DataFrame 'df'
df = pd.DataFrame({
    'keyword': ['w1', 'w2', 'w3'],
    'frequency': [10, 8, 6]
    })

pt.bar(df['keyword'], df['frequency'])
pt.xlabel('keyword')
pt.ylabel('frequency')
pt.title('keyword.')
pt.show()
