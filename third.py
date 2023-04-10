a = 0
numbers = []
while a != 'end':
    a = input("Write number (or \"end\"):")
    try:
        numbers.append(int(a))
    except:
        pass
print(numbers)