user_name = input("Please enter your name: ")
print(f"Hey there, {user_name}!")

user_age = input("How old are you? ")

try:
    user_age = int(user_age)  # Attempting to convert input to an integer
    # risky_calculation = 100 / 0  # Uncommenting this line would cause a ZeroDivisionError
except ValueError:
    print("Oops! That doesn't seem like a valid number.")

except ZeroDivisionError:
    print("Math error! Division by zero is not allowed.")

except:
    print("An unexpected error occurred. Please try again.")

else:  # Executes if no exceptions occur
    print(f"You were likely born in {2024 - user_age}.")

finally:
    print("Game over. Thanks for playing!")