# print ('Hello World!')

# numbers = list(range(0, 30))
# new_list = []
# for num in numbers:
#     if len(new_list) > 4:
#         print(f'We have enough even numbers in new_list ({len(new_list)}). break will stop the for loop now')
#         break
#     elif num % 2 == 0:
#         new_list.append(num)
#     elif num % 2 != 0:
#         continue
#         print('i never get executed')
#     print(num, 'is even.')
#     print('this does not print for odd numbers\nbecause the continue statement skips\nthe code that follows in the for loop\nand goes straight back to the next element in the for loop')
    

# for i in list(range(0, 5)):
#     if True:
#         print(i)
#         break
#     print("I'll never get executed either")

# names = ['aNNE', 'JaNe', 'willIAM', 'WanDA', 'WeSt', 'HELEN', 'tHoMaS', 'HENrY', 'John', 'Marshall', 'May']
# formatted_names = []
# check_count = 0

# for name in names:
#     if name.startswith('w') or name.startswith('W'):
#         check_count += 1
#         continue
#     elif len(formatted_names) >= 4:
#         check_count += 1
#         break
#     else:
#         formatted_names.append(name.title())

# print('before', names)
# print('after', formatted_names)
# print(check_count)

# people = [
#     {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"}, 
#     {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
#     {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
#     {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
#     {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
#     {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
# ]
# first_dog_person = None
# iteration_count = 0
# for person in people:
#     iteration_count += 1
#     if person['pet'] == 'Dog':
#         print('{} has a dog! Had to check {} records to find a dog owner.'.format(person['name'], iteration_count))
#         break

# programmers = [{'name': "rachel", 'favorite_languages': ['Ruby', 'JavaScript', 'SQL', "Java"]},
#                {'name': "daniel", 'favorite_languages': ['JavaScript', 'Elixir', 'Python']},
#                {'name': "greg", 'favorite_languages': ['C#', 'CoffeeScript', 'R']},
#                {'name': "meryl", 'favorite_languages': ['C++', 'PHP', 'Swift']}
#               ]

# for programmer in programmers:
#     # for language in programmer['favorite_languages']:
#         print(programmer)

# outer = 0
# inner = 0
# while outer < 3:
#     outer += 1
#     print("outer iteration:", outer)
#     while inner < 3:
#         inner += 1
#         print("    inner iteration:", inner)
#     inner = 0
#     print("\n")

# name = "Joe"

# def greeting(name):
#     print(f"Hello, {name}")
# greeting("Sophie")

# evil_monster = "Bowser"

# def princess_peachs_castle():
#     print(f"{evil_monster} is trying to kidnap Princess Peach!")
# princess_peachs_castle()

change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"
change_yourself()
print(change_the_world)
