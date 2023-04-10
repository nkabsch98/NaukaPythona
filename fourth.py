number = input("Enter some big number: ")
j = len(number)-1
palindrome = True
for i in range(len(number)):
    if number[i] != number[j]:
        palindrome = False
    j-=1
if palindrome:
    print(number,"is palindrome")
else:
    print(number,"is not palindrome")

