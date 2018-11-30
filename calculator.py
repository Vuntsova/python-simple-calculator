num1 = float(input('Enter first number: '))
op = input('Enter operator(- + / *): ')
num2 = float(input('Enter second number: '))

if op == '+':
    results = num1 + num2
elif op == '-':
    results = num1 - num2
elif op == '/':
    results = num1 / num2
elif op == '*':
    results = num1 * num2
else:
    results = 'Invalid Operator'


print(results)
