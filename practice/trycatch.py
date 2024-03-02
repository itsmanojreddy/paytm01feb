i = 10
try:
    print(i / 0)
except IndentationError:
    print("cannot be divisible by 0")
except:
    print("Programm is executed")

