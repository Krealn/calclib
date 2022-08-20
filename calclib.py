def calc():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("Enter function (+, -, /, *): ")
    if c == "+":  print(int(a) + int(b))
    if c == "-":  print(int(a) - int(b))
    if c == "*":  print(int(a) * int(b))
    if c == "/":
        try:
            print(int(a) / int(b))
        except:
            print("Dont try division to zero!")
            
def returnCalc():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("Enter function (+, -, /, *): ")
    if c == "+":  d = int(a) + int(b)
    if c == "-":  d = int(a) - int(b)
    if c == "*":  d = int(a) * int(b)
    if c == "/":
        try:
            d = int(a) / int(b)
        except:
            d = "Dont try division to zero!"
    return d