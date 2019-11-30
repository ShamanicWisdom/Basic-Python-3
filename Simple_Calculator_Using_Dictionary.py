# Switch-like simple two-argument calculator (using dictionary).
def addition():
    try:
        print("Addition:")
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value + second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g + %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def subtraction():
    try:
        print("Subtraction:")
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value - second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g - %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def multiplication():
    try:
        print("Multiplication:")
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value * second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g * %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def division():
    try:
        print("Division:")
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        if second_value == 0:
            print("Cannot divide by zero!")
        else:
            result = first_value / second_value
            # %g will ignore trailing zeroes.
            print("\nResult of %.5g / %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("\nPlease insert  proper numbers!\n")

def finish():
    print("\nExiting the program...\n")
    exit()

#Dictionary - binding function name to specific number.
all_functions = {1: addition, 2: subtraction, 3: multiplication, 4: division, 0: finish}

print("==Calculator==")
while True:
    try:
        print("1. Addition.")
        print("2. Subtraction.")
        print("3. Multiplication.")
        print("4. Division.")
        print("0. Exit.")
        user_choice = int(input("Please input a number: "))
        all_functions[user_choice]()
    except ValueError:
        print("\nProgram will accept only integer numbers as an user choice!\n")
    except KeyError:
        print("\nNo function binded to this number! Try again.\n")