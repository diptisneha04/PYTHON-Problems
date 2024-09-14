import pandas as pd
file=open("C:/Users/ASUS/Downloads/Sentences.txt","r",encoding="UTF-8")
s= file.read()
l=len(s)
list=[]
for i in (0,l):
    for j in range(i,l):
        list.append(s[i:j+1])
print(list)
    
