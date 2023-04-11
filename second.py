#variables declaration
vowels = ['a', 'e', 'i', 'o', 'u']
text = input("Write sentence: ")
text_vowels = []
text_consoants = []

#for loop to check letters in string
for i in text:
    if i.lower() in vowels:
        text_vowels.append(i)
    else:
        text_consoants.append(i)

#printing results
print("Vowels in text: ",list(dict.fromkeys(text_vowels)))
print("Consoants in text: ",list(dict.fromkeys(text_consoants)))

