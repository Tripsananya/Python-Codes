guests=[("Alice",28),
        ("Bob",22),
        ("Eve",35),
        ("Dave",45),
        ("Grace",24),
        ("Hellen",30)]

list1=[]
list2=[]

for name, age in guests:
    if age<30:
        list1.append(name)
    else:
        list2.append(name)

print(list1)
print(list2)
