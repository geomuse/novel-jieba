import matplotlib.pyplot as pt
from matplotlib import style
import pandas as pd
style.use('ggplot')

# 假设你有一个包含列 'Sentiment' 和 'Count' 的 DataFrame 'df'
df = pd.DataFrame({'sentiment': ['positive', 'neutral', 'negative'], 'count': [30, 20, 10]})

pt.pie(df['count'], labels=df['sentiment'], autopct='%1.1f%%', startangle=90, colors=['green', 'gray', 'red'])
pt.axis('equal')
pt.title('sentiment')
pt.show()