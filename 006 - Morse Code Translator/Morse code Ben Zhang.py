#Morse Code
#str。split
while 1==1:
    dict = {'A': '·-',     'B': '-···',   'C': '-·-·','D': '-··',    'E': '·',      'F': '··-·',
        'G': '--·',    'H': '····',   'I': '··','J': '·---',   'K': '-·-',    'L': '·-··',
        'M': '--',     'N': '-·',     'O': '---','P': '·--·',   'Q': '--·-',   'R': '·-·',
        'S': '···',    'T': '-',      'U': '··-','V': '···-',   'W': '·--',    'X': '-··-',
        'Y': '-·--',   'Z': '--··',
        '0': '-----',  '1': '·----',  '2': '··---','3': '···--',  '4': '····-',  '5': '·····',
        '6': '-····',  '7': '--···',  '8': '---··','9': '----·'
        }
    code = input('Letters: ')
    list = []
    for i in code:
        if i==' ':
            list.append(' ')
        else:
            list.append(dict[i.upper()])
    print(' '.join(list))
