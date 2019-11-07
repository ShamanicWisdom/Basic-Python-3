# IF-ELSE simple two-argument calculator.
def addition():
    try:
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value + second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g + %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def subtraction():
    try:
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value - second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g - %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def multiplication():
    try:
        first_value = float(input("Input the first value: "))
        second_value = float(input("Input the second value: "))
        result = first_value * second_value
        # %g will ignore trailing zeroes.
        print("\nResult of %.5g * %.5g is: %.5g\n" % (first_value, second_value, result))
    except ValueError:
        print("Please insert  proper numbers!")


def division():
    try:
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


print("==Calculator==")
user_choice = -1
while user_choice != 0:
    print("1. Addition.")
    print("2. Subtraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("0. Exit.")
    try:
        user_choice = int(input("Please input a number: "))
        if user_choice not in [0, 1, 2, 3, 4]:
            print("\nPlease input a proper choice!\n")
        else:
            if user_choice == 0:
                print("\nExiting the program...\n")
            else:
                if user_choice == 1:
                    addition()
                else:
                    if user_choice == 2:
                        subtraction()
                    else:
                        if user_choice == 3:
                            multiplication()
                        else:
                            if user_choice == 4:
                                division()
    except ValueError:
        print("\nProgram will accept only integer numbers as an user choice!\n")