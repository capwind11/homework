import os
import collections
path = 'D:\\大三上\\自然语言处理\\text\\'
l = os.listdir('D:\\大三上\\自然语言处理\\text')
print(l)
f = open('total.txt','w',encoding='utf-8')
dict = {}
for i in l[:10]:
    tmp = open(path+i,'r',encoding='utf-8')
    text = ''.join(tmp.readlines())
    for i in text:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    tmp.close()
f.write(str(dict))
f.close()




