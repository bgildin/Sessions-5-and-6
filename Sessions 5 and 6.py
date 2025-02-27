name = input("What is your name? ")
print("Hello", name)
age = input("How old are you? ")
try:
    age = int(age)
except:
    print("You are trying to trick me ")
    print("Better luck next time ")

    print("something unexpected happened ")
else:
    print("you were probably born in ", 2024 - age)
finally:
    print("thanks for playing")
