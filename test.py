#print("hello phyton")

num1 = float(input("firstint : "))
num2 = float(input("secondint : "))
symbol = input("+,-,%,*,/")

if symbol == "-":
    num = num1 - num2
    print(num)
elif symbol == "+":
    num = num1 + num2
    print(num)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "/":
    print(num1 / num2)
else:
    print("im sorry")





