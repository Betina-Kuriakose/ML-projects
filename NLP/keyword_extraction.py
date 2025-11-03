import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/Tesla'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Create a request with headers
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html=response.read()# here it reads the data along with HTML content
# print(html)
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)
# print(text)
tokens=[t for t in text.split()]
print(tokens)
sr=stopwords.words('english')
clean_tokens=tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq=nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key)+":"+str(val))
freq.plot(20, cumulative=False)
plt.show()

