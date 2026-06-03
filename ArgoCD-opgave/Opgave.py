import time


myMessage = "self destructing in"


print("Hello, World!")

for i in range(10, -1, -1):
    time.sleep(1)
    print(myMessage + " " + str(i) + " seconds...")

value = i

if value == 0:
    print("BOOM! Self destructed!")

#testtest