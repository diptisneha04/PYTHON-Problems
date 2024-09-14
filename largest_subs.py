st="snehaa"
l=len(st)
lt=[]

for i in range (0,l):
    for j in range(i,l):
        lt.append(st[i:j+1])
print(lt)        

d={}
for i in lt:
    if i in d:
        d[i]=d.get(i,0)+1
        
        
large_sub = max((sub for sub in d.items()),key=len)       
print(f"Largest substring: {large_sub}")        



"""
    else:
        d[i]=1
large_sub = max((sub for sub,freq in d.items() if len(sub) == len(st) ), key=len)    

print(f"Largest substring: {large_sub}")

        """