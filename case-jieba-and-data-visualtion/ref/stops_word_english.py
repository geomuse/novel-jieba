import nltk
from nltk.corpus import stopwords

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
nltk.data.path.append(path)
nltk.download('stopwords',download_dir=path)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

path = "/home/geo/Downloads/geo/text_mining_bot/ntlk_data" 
text = "This is a sample sentence with some neutral and meaningless words."
filtered_text = remove_stopwords(text)
print(filtered_text)