# getting the input from the user.
input = str(input("Enter the name:"))


list = ["prabin","subedi"]
# appendig the input to the list.
list.append(input)
print(list)
dict = {'name':'sachin','age':22,'city':'Khambe Danda'}
# removing the age key value pair from the dict.
dict.pop('age')
# upcdating the name key value pair with the input.
dict.update({'name':input})
print(dict)

string = "prabin is very good and loving husbando your not riterally ryan gosring "
# getting the count of "a"s in the string.
countOfA=string.count('a')
print(countOfA)
