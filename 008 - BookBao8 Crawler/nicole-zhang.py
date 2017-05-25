import requests
from bs4 import BeautifulSoup
url = input('URL: ')
web = requests.get(url)
web.encoding = 'gb18030'
soup = BeautifulSoup(web.text, 'html.parser')
a = soup.select('dd#contents')[0]
a = a.get_text()
b = soup.select('h1')[0]
b = b.get_text()
def text_create(name, msg):   
    desktop_path = '/Users/NicoleZhang/Desktop/'    
    full_path = desktop_path + name + '.txt' 
    file = open(full_path,'w', encoding= 'utf8')             
    file.write(msg) 
    file.close()
text_create(b , a)
