x = 10  #змінна integer
y = 2.5 #змінна float
str_value = "Hello World" # рядок str
str_number = int("5") #рядок з числом і типом int

sum_res = x + y
sub = x - y
mul = x * y
div = x / y

str_sum_res = str_value + " i`m phyton" #з'єднання рядка
str_mul_res = (str_value + " ") * 3 # дублювання рядка

print(f"додавання x + y: {sum_res}")
print(f"віднімання x - y: {sub}")
print(f"множення x * y: {mul}")
print(f"ділення x / y: {div}")
print(f"дублювання рядка {str_mul_res}")
print(f"з'єднання рядка {str_sum_res}")

user_input = input("введіть число")

print(f"ваше число {user_input} тип данних input:{type(user_input)}")
