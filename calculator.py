import os

def calculator():
    global first, second, algorithm, sum, history, repeat, delete_history
    first = float(input("First number: "))
    second = float(input("Second number: "))
    algorithm = str(input("Algorithm (+, -, *, /): "))
    sum = 0

    if algorithm == "+":
        sum = first + second
    elif algorithm == "-":
        sum = first = second
    elif algorithm == "*":
        sum = first * second
    elif algorithm == "/":
        sum = first / second
    print(f"The sum is {sum}")
    history = str(input("Do you want to save the history (y/n): "))

    if history == "y":
        if not os.path.exists("history.txt"):
            f = open("history.txt", "w")
            f.write(f"This is the oldest sum: {sum}")
            f.close()
            print("History has been saved.")
        elif os.path.exists("history.txt"):
            f = open("history.txt", "a")
            f.write(f"; {sum}")
            f.close()
            print("History has been saved.")
    elif history == "n":
        print("Okay.")
    else:
        print("There's an error.")

    delete_history = str(input("Do you want to delete the history (y/n): "))

    if delete_history == "y":
        if os.path.exists("history.txt"):
            os.remove("history.txt")
            print("History has been deleted.")
        else:
            print("You didn't save history or you deleted history so I can't delete it.")
    elif delete_history == "n":
        print("Okay.")
    else:
        print("There's an error.")

    repeat = str(input("Do you want to use calculator again (y/n): "))

    if repeat == "y":
        calculator()
    elif repeat == "n":
        print("Okay.")
    else:
        print("There's an error.")

calculator()
