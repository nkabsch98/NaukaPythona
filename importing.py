from objective import Dog


new_dog = Dog("max",5)
new_dog.voice()
print(new_dog.name)
old_dog = Dog("Tom", 4)
third_dog = Dog("Eric", 8)
my_dogs = []
my_dogs.append(new_dog)
my_dogs.append(old_dog)
my_dogs.append(third_dog)
print(list(dog.age for dog in my_dogs))