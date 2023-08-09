# Run a loop and ask an input to the user. Then, write that input into a file. Stop the loop if user inputs 'quit'
fileNameToWrite = "day4.txt"
inputList= []
userInput = input("Enter a string: ")
while userInput != "--quit":
    inputList.append(userInput)
    userInput = input("Enter a string: ")

print("Writing to file...")
with open(fileNameToWrite, "w") as file:
    for i in inputList:
        file.write(i + "\n")
print(f"File written successfully to {fileNameToWrite} !")
