from wordcloud import WordCloud
import matplotlib.pyplot as pt
from matplotlib import style
style.use('ggplot')

text = "write your work in here."
wordcloud = WordCloud(width=800,height=400,background_color='white').generate(text)

pt.figure(figsize=(10, 5))
pt.imshow(wordcloud, interpolation='bilinear')
pt.axis('off')
pt.show()

