morse = {'.-': 'a', '-...': 'b', '-.-.': 'c', '.': 'd'}
word = input(':')
result = ''

for i in word.split('   '):
    for a in i.split():
        result = result + morse[a]
    result = result + ' '
        
print(result)
