try:
    newFile = open("newfile.txt", "x", encoding="utf-8")
except OSError:
    newFile = open("newfile.txt", "w", encoding="utf-8")
text = ""
for i in range(255):
    text = text + str(i) + " - " + chr(i) + "\n"
print(text)
newFile.write(text)