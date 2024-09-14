st="the weather is foggy and I dont like this weather"

st1=st.split()

longest_word=" "
for i in st1:
    if len(i) > len(longest_word):
        longest_word=i
        
print("longest word is:",longest_word,"\n")


    
    

    
    
