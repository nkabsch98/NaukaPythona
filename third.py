a = 0
numbers = []

#Entering numbers from the keyboard until "end" appears
while a != 'end':
    a = input("Write number (or \"end\"):")
    try:
        numbers.append(int(a))
    except:
        pass
topNumber = numbers[0]
lowNumber = numbers[0]
duplicates = []
#Iterating trough numbers to find max, lowest and duplicates
for i in numbers:
    counter = -1
    if i > topNumber:
        topNumber = i
    elif i < lowNumber:
        lowNumber = i
    for j in numbers:
        if j == i:
            counter+=1
    if counter > 0 and i not in duplicates:
        duplicates.append(i)
print("Max number:",topNumber)
print("Lowest number:",lowNumber)
print("Duplicates:",duplicates)
    