firstNum=int(input("Enter the first number : "))
secondNum=int(input("Enter the second number : "))
result=firstNum*secondNum
print( firstNum , " x " , secondNum , " = " , result)

if result>0 :
    print("The result is positive.")
elif result<0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")