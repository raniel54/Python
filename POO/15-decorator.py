from decorator import my_decorator, uppercase_decorator, split_string

# exemplo 1
@my_decorator
def my_function():
    print("dentro da função")
my_function()

#Exmplo 2 
@uppercase_decorator
def text():
    return "hello world"
print(text())

#excmplo 3
@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())