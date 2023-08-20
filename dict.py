pizza_price={
    'small':8.99,
    'medium':12.99,
    'large':15.99
}

'''
num=int(input("Please enter the number of pizzas: "))
size=(input("Please enter the size of pizza: "))

if size=="small":
    total=num*pizza_price["small"]
    print("TOTAL: ",total)

elif size=="medium":
    total=num*pizza_price["medium"]
    print("TOTAL: ",total)

elif size=="large":
    total=num*pizza_price["large"]
    print("TOTAL: ",total)

else:
    print("GHAR PE JA KE BANAO......")

'''




#using for loop->


for i in pizza_price:
    num=int(input("Please enter the number of pizzas: "))
    size=(input("Please enter the size of pizza: "))


    if size=="small":
        total1=num*pizza_price["small"]
        

    elif size=="medium":
        total2=num*pizza_price["medium"]
        

    elif size=="large":
        total3=num*pizza_price["large"]
        

    else:
        print("GHAR PE JA KE BANAO......")

print("TOTAL: ",total1)
print("TOTAL: ",total2)
print("TOTAL: ",total3)

grandtotal=total1+total2+total3

print("Sub Total amount: ",grandtotal)




