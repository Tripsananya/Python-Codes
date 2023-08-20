'''num=int(input("Enter the number: "))


if (num & 1):
    print("odd")

else:
    print("even")
'''

num=int(input("Enter the number: "))
num2=int(input("Enter the number: "))

num=num^num2       #num^=num2
num2=num2^num
num=num^num2

print(num,num2)
    
