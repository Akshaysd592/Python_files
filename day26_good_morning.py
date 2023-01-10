import time
timestamp  = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))

if((timestamp>=0)and(timestamp<12)):
    print("Good Morning sir")
elif((timestamp>=12) and (timestamp<=17)):
    print("Good Afternoon sir")
else:
    print("Good Evening sir")
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)



