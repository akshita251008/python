string = input("please enter your own string : ")
string2 = ('')

for i in string:
    string2 = i + string2

print("\nthe oringinal string = ", string)
print("the reversed string = ", string[::-1])
print("the reversed string = ", string2)