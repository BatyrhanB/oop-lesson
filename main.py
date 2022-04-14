from calculator import Calculator # Imported methods
import random # Imported random for create random list

rand_list = [] # created empty list
for i in range(20):
    '''Apend 20 random nambers to list'''
    rand_num = random.randint(1,100)
    rand_list.append(rand_num)

# Inicalization class (created objects)
add = Calculator.addition(*rand_list)
sub = Calculator.subtraction(*rand_list)
mul = Calculator.multiplication(*rand_list)
div = Calculator.division(*rand_list)

print(f"Numbers: {rand_list}\n") #show list
print(f"Sum: {add}\nDifference: {sub}\nProduct: {mul}\nQuotient: {div}") #show resullts