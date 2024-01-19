import jieba

# def remove_chinese_stopwords(text):
#     ...
#     return ' '.join(filtered_words)

# 示例
# text = "这是一句包含一些中性和无意义词的例句。"
# filtered_text = remove_chinese_stopwords(text)
# print(filtered_text)

documents_path ='/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/input_novel.md'
stop_words_path = '/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/stop_words.txt'

with open(documents_path,'r',encoding='utf-8') as f:
    content = f.read()

with open(stop_words_path,'r',encoding='utf-8') as f:
    stops = f.read()

def remove_chinese_stopwords(text):
    words = jieba.lcut(text)
    filtered_words = [word for word in words if word not in stops]
    return ' '.join(filtered_words)

contents = remove_chinese_stopwords(text=content)

with open("/home/geo/Downloads/geo/text_mining_bot/case-jieba-and-data-visualtion/result_remove_stopwords.txt",'w',encoding='utf-8') as f :
    for _ in content :
        f.write(f'{str(_)}\n')

"""
import jieba

def remove_chinese_stopwords(text):
    # 你可以使用自己的中文停用词表
    stop_words = set([
        '的', '了', '和', '是', '在', '有', '不', '我', '他', '我们', '你', '他们', '这', '那', '就', '吧'
        # 添加其他停用词...
    ])
    
    words = jieba.cut(text)
    filtered_words = [word for word in words if word not in stop_words]
    
    return ' '.join(filtered_words)

# 示例
text = "这是一句包含一些中性和无意义词的例句。"
filtered_text = remove_chinese_stopwords(text)
print(filtered_text)
"""