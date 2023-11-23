# This program will help a grade school student practice the four
# basic operations (addition, subtraction, multiplication, and division).
import random

choices = input(str('Choose if what do you want this program to perform'
                    '\n[1] Addition'
                    '\n[2] subtraction'
                    '\n[3] Multiplication'
                    '\n[4] Division'
                    '\nEnter Here:'))

if choices == 1:
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)

    # Asks the user to enter answer
    answer = eval("What is" + str(number1) + "+" + str(number2) + "?")

    # Display result
    print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

elif choices == 2:
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)

    # Asks the user to enter answer
    answer = eval("What is" + str(number1) + "-" + str(number2) + "?")

    # Display result
    print(number1, "-", number2, "=", answer, "is", number1 - number2 == answer)

elif choices == 3:
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)

    # Asks the user to enter answer
    answer = eval("What is" + str(number1) + "*" + str(number2) + "?")

    # Display result
    print(number1, "*", number2, "=", answer, "is", number1 * number2 == answer)

elif choices == 4:
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)

    # Asks the user to enter answer
    answer = eval("What is" + str(number1) + "/" + str(number2) + "?")

    # Display result
    print(number1, "/", number2, "=", answer, "is", number1 / number2 == answer)

else:
    print("Answer is invalid.Refer to the choices.")
    import sys
    sys.exit()
