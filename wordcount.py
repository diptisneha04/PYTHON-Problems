str="My name is sneha and I like my name "
st1=str.split()

d={}
for word in st1:
    if word in d:
        d[word]+=1
    else:
        d[word]=1
 
for key,value in d.items():
    print(f"{key} : {value}")        