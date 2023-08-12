import os
def OpenCalculatorProgram():
    os.system("open /System/Applications/Calculator.app")


def multipleOfFive(a)->int:
    return a*5

def multiplesOfFive(multipleOfFive,b)->list:
    return list(map(multipleOfFive,b))

inputList = [1,2,3,4,5,6,7,8,9,10]

print("Press 1 to open a program.")
print("Enter 2 to find multiples of 5 ")
choice = int(input("Enter your choice: "))
if choice == 1:
        OpenCalculatorProgram()
elif choice == 2:
    print(multiplesOfFive(multipleOfFive,inputList))

else:
    print("Invalid choice.")
