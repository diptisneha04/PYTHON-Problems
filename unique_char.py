str="GoodMorning"
char_count = {}
for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

    unique_count = len(char_count)
print("Unique count:",unique_count)    