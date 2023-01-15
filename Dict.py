mydict = {"name": "Max", "age": 28, "city": "New York"}

for key, value in mydict.items():
    print(mydict)

mydict_cpy = mydict
print(mydict_cpy)

mydict_cpy["email"] = "max@gmail.com"
print(mydict_cpy)
print(mydict)



mydict = {"name": "Max", "age": 28, "city": "New York"}

mydict_cpy = mydict.copy()
print(mydict_cpy)

mydict_cpy["email"] = "max@gmail.com"
print(mydict_cpy)
print(mydict)


my_dict = {"name": "Max", "age": 28, "email": "max@gmail.com"}
my_dict_2 = dict(name="Max", age=27, city= "boston")

my_dict.update(my_dict_2)
print(my_dict)


my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

my_typle = [8, 7]
my_dict = {my_typle: 15}

print(my_dict)