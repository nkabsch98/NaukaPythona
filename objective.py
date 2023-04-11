
#declaring main class
class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#declaring child classess
class dog(animal):
    def voice(self):
        print("woof",end=" ")

class cat(animal):
    def voice(self):
        print("meow",end=" ")

#asking user basic questions about animal
animal_type = input("Is your animal cat or dog? ")
animal_name = input("What is the name of your " + animal_type + "? ")
animal_age = input("How old is "+ animal_name + "? ")

#animals creation
if animal_type == "cat":
    pet = cat(animal_name,animal_age)
elif animal_type == "dog":
    pet = dog(animal_name, animal_age)

#using dog or cat function
pet.voice()
print("-",pet.name,"said")