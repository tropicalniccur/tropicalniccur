print("elcome: complex calculator")
while true:

    try:
        int_one = int(input("enter first number: "))
        int_two = int(input("enter second number: "))
        op = input("enter operation, options:{+,-,*,/,%}")
        if op =="+":
            print(int_one+int_two)
        elif op =="-":
            print(int_one-int_two)
        elif op =="*":
            print(int_one*int_two)
        elif op =="/" :
            print(int_one/int_two)
        elif op =="%":
            print(int_one%int_two)
        else:
            print("operation does not exist")

    exept valueError:
        print("value error")
    exept zeroDivisionError:
        print("Division by zero is not possible")