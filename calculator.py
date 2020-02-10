print ('Enter number 1')
number1 = int(input())

print('Do you want to add +, subtract -, multiply * or divide /')
operator = str(input())

print('Enter number 2')
number2 = int(input())

if operator == '+':
    print (number1 + number2)
elif operator  == '-':
    print (number1 - number2)
elif operator == '*':
    print (number1 * number2)
elif operator == '/':
    print (number1 / number2)
