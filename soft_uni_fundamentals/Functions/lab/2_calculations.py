def calculation(operator, n1, n2):
    if operator == 'multiply':
        result = n1 * n2
    elif operator == "divide":
        result = n1 // n2
    elif operator == "add":
        result = n1 + n2
    elif operator == "subtract":
        result = n1 - n2
    return result


command = input()
num1 = int(input())
num2 = int(input())

print(calculation(command, num1, num2))
