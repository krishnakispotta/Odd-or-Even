def action():
    print("What number you are thinking?")
    x = int(input())
    if x%2 == 0:
        print("That's an Even Number! Have another?")
    else:
        print("That's an Odd Number! Have another?")

def choice():
    print("Type 'Y' or 'N'")
    p = input()
    if p == "y" or p == "Y":
        action()
        choice()
    elif p =="n" or p =="N":
        exit()
    else:
        print("Please enter valid Choice")
        choice()

action()
choice()
