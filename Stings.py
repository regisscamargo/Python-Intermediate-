my_stign = """Im a programer"""
print(my_stign)

char = my_stign[-2]
print(char)

substring = my_stign[1:5]
print(substring)

#reverse

my_stign[::-1]
print(my_stign)


greeting = "hello"
name = "tom"
sentence = greeting + "" + name
print(sentence)

if 'n' in greeting:
    print('yes')

else:
    print('no')

my_string = '    Hello Workd   '
my_stign = my_stign.strip()
print(my_stign)

my_stign = 'Hello Word'
print(my_stign.startswith('Hello'))

my_stign = 'Hello Word'
print(my_stign.find('o'))

my_stign = 'Hello Word'
print(my_stign.replace('Word', 'Universe'))

my_stign = 'how are you doing'
my_list = my_stign.split()
print(my_list)

my_stign = 'how are you doing'
my_list = my_stign.split(',')
new_string = ''.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

#bad

my_string = ''
for i in my_list:
    my_string += i
print(my_string)

#good

my_string = ''.join(my_list)
print(my_list)

# %, .format(), f-strings
var = 'tom'
my_string = 'the variable is %s' % var
print(my_string)

var = 3.123456
my_string = 'the variable is %f' % var
print(my_string)

var = 3.123456
my_string = 'the variable is %2f' % var
print(my_string)

var = 3.123456
my_string = 'the variable is {}'.format(var)
print(my_string)

var = 3.123456
my_string = 'the variable is {:.2f}'.format(var)
print(my_string)

var = 3.123456
var2 = 6
my_string = 'the variable is {:.2f} and {}'.format(var, var2)
print(my_string)

var = 3.123456
var2 = 6
my_string = f'the variable is {var} and {var2}'.format(var, var2)
print(my_string)

var = 3.123456
var2 = 6
my_string = f'the variable is {var*2} and {var2}'.format(var, var2)
print(my_string)