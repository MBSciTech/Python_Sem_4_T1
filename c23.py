#Word cloud
from wordcloud import WordCloud, STOPWORDS
import requests
import matplotlib.pyplot as plt

url = 'https://www.gutenberg.org/files/11/11-0.txt'
response = requests.get(url)
text = response.text 
# print(text)
stopwords = set(STOPWORDS)
# print(stopwords)

alice = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords,

)

alice.generate(text)
plt.imshow(alice)
plt.axis('off')
plt.show()


stopwords.add('said')
alice.generate(text)
fig = plt