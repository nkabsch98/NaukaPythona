try:
    newFile = open("newfile.txt", "r", encoding="utf-8")
except OSError:
    print("File does not exist!")

print(newFile.read())