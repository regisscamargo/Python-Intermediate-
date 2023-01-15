x = -5
assert (x>=0), 'X is not positive'

try:
    a = 5 /1 
    b = a + 4

except ZeroDivisionError as e:
    print(e)

except TypeError as e:
    print(e)

else:
    print('Aqui está tudo certo')

finally:
    print('cleaning up....')