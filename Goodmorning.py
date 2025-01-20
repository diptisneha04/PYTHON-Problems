import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
if (timestamp<12):
    print("Good Morning!")
    
else:
    print("Good Afternoon!")