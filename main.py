"SIMPLE CALCULAOTR"
while True:
 a=float(input("Enter a first  number:"))
 b=float(input("Enter a second  number:"))
 print("Select your operation to be performed (+, -, *, /, %, //):")
 opr=input("Enter operator:")


 if opr=='+':
    print(f'sum is :{a} + {b} = {a+b}')

 elif opr=='-':
    print(f'subtract is:{a} - {b} = {a-b}')

 elif opr=='*':
    print(f'Multiplication is:{a} * {b} = {a*b}')

 elif opr=='/':
    if b==0:
        print("Cannot divide by zero ❌")
    else:
        print(f'Division is:{a} / {b} = {a/b}')

 elif opr=='%':
    print(f'Modulus  is:{a} % {b} = {a%b}')

 elif opr=='//':
    if b == 0:
        print("Cannot divide by zero ❌")
    else:
        print(f'Floor division is: {a} // {b} = {a//b}')
 else:
    print("Invalid operator ❌")

 again=input("Do you want any other calculation? (y/n): ").lower()
 if again !='y':
    print("Exiting calculator. Goodbye! 👋")
    break



