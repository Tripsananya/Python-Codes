num1=int(input("Enter the First Number: "))
num2=int(input("Enter the Second Number: "))
num3=int(input("Enter the Third Number: "))

if num1>num2 and num1>num3:
    print("{0} is the largest number among {1},{2},{3}".format(num1,num1,num2,num3))

elif num2>num1 and num2>num3:
    print("{0} is the largest number among {1},{2},{3}".format(num2,num1,num2,num3))

else:
    print("{0} is the largest number among {1},{2},{3}".format(num3,num1,num2,num3))
