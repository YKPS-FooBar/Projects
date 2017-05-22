#decode
morse = {'.-': 'a', '-...': 'b', '-.-.': 'c', '.': 'd'}
word = input(':')
result = ''

for i in word.split('   '):
    for a in i.split():
        result = result + morse[a]
    result = result + ' '
        
print(result)

#incode
morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'.'}
word = input(': ')
word = word.lower()
length = len(word)
n = 0
x = ''
while n < length:
    x = x + morse[word[n]] + '  ' 
    n = n + 1
print(x)
