#Importere time biblioteket for at kunne bruge sleep-funktionen
import time


myMessage = "self destructing in"

# Printer "Hello, World!"
print(("Hello, World!"), flush=True)

# for-loop
for i in range(10, -1, -1):
    time.sleep(1)
    print((myMessage + " " + str(i) + " seconds..."), flush=True)

value = i

# Branching if-statement
if value == 0:
    print(("BOOM! Self destructed!"), flush=True)
