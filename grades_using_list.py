grade=[70,77,60,65,30,35]
list1=[]
list2=[]

for i in grade:
    if i<70:
        list1.append(i)

    else:
        list2.append(i)

print("Number smaller than 70 -> ",list1)
print("Number greater than 70 -> ",list2)
