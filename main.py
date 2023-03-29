import random

code = [random.randint(0, 9), random.randint(0, 9), random.randint(0,9), random.randint(0,9)]
code = [1, 1, 1, 1]
CurrentCode = [0, 0, 0, 0]
userCode = [0, 0, 0, 0]

def checkCode(place1, place2, place3, place4):
    check = 0

    if place1 == code[0]:
        check += 1
        CurrentCode[0] = code[0]

    if place2 == code[1]:
        check += 1
        CurrentCode[1] = code[1]

    if place3 == code[2]:
        check += 1
        CurrentCode[2] = code[2]

    if place4 == code[3]:
        check += 1
        CurrentCode[3] = code[3]

    if check == 4:
        return True

    else:
        return False

print("                               Code Guesser                               ")
print("")
print("------------------------------- Directions --------------------------------")
print()
print("1) You have to guess the 4 diget code")
print("2) It will show when you have the digets correct and which ones are correct")
print("\n\n")


while checkCode(userCode[0], userCode[1], userCode[2], userCode[3]) == False:
    userCode[0] == int(input("Enter the first diget of the code (0 - 9): "))
    userCode[1] == int(input("Enter the second diget of the code (0 - 9): "))
    userCode[2] == int(input("Enter the third diget of the code (0 - 9): "))
    userCode[3] == int(input("Enter the forth diget of the code (0 - 9): "))




