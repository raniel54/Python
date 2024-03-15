num1 = float(input("Digite o numero 1\n"))
num2 = float(input("Digite o numero 2\n"))
operation = input("Digite a operacao a realizar ( + - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operacao invalida")
    result = 0
print(f"Resultado e: {result:.2f}")