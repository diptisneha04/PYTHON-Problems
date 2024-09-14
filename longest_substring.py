st = "sneha"

l = len(st)
lst = []

for i in range(0, l):
    for j in range(i, l):
        lst.append(st[i:(j + 1)])
print(set(lst))
largest_sub = ""
count = 0
lst1=set(lst)
for sub in lst1:
    if len(sub) > len(largest_sub):
        largest_sub = sub
        
    if len(sub) == len(largest_sub):
        count += 1

print("Longest substring is:", largest_sub)
print("Frequency of the longest substring:", count)

