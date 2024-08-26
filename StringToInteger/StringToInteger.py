user_input = input("TYPE ANY INTEGER!!   ")
#Gets the user input, but any input is a string
integer = int(user_input)
#Makes the string an integer by making what was a string an integer
print(integer)
print("Now that this is an integer instead of a string, you can use it for math!")
print(integer*integer)
print(integer+integer)
answer = input("Do you want to do this for your project? Want the source code? y/n")
if answer == 'y':
    print("https://github.com/Sdmonke/StringToInteger")
if answer == 'n':
    print("That's fine!")