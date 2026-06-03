import time


myMessage = "self destructing in"

print("Hello, World!")

print("i will self destruct in 10 seconds...")

for i in range(10, 0, -1):
    time.sleep(1)
    print(myMessage + " " + str(i) + " seconds...")

print("Goodbye, World!")