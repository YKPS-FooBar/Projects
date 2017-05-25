#Spyder

import requests
emput = input('Website:')
web = requests.get(emput)
web.encoding = 'gb18030'
from bs4 import BeautifulSoup
txt = BeautifulSoup(web.text,"html.parser")
a = txt.select('dd#contents')[0]
a = a.get_text().replace('<br/>', '\n')
n = txt.select('dd > h1')[0]
n = n.get_text().replace('</a>', ' ')
n = n.replace('</h1>', ' ')
n = n.replace('<h1>', ' ')
#print(n)
#print(a)
tt=(n+'\n'+a)
with open(n+'.txt', 'w',encoding='gb18030') as text_file:
    text_file.write(tt)
    
     
