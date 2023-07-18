#Lists
numbers = [i+1 for i in range(20)]
people = [
    {"name":"Rob", "age":16},
    {"name":"Mike", "age":26},
    {"name":"Tom", "age":39},
    {"name":"Anna", "age":17},
    {"name":"Maria", "age":22},
    {"name":"Rob", "age":28},]

#Normal way
def square(numbers):
    squared_numbers = []
    for i in numbers:
        squared_numbers.append(i**2)
    return squared_numbers

def even(nums):
    even_nums = []
    for i in nums:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

def ages(people):
    people_ages = []
    for person in people:
        people_ages.append(person["age"])
    return list(people_ages)

#Comprehension way

comp_squared_numbers = [i**2 for i in numbers]
comp_even_numbers = [i for i in numbers if i % 2 == 0]
comp_people_ages = [person["age"] for person in people]

#Prints

print(list(square(numbers)))
print(comp_squared_numbers)
print(list(even(numbers)))
print(comp_even_numbers)
print(ages(people))
print(comp_people_ages)



 