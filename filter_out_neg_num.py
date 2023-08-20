number=[5,-2,10,-8,7,-3]
a=number[:]
for i in number:
    if i<0:
        a.remove(i)
        continue
    else:
        print(i)

print(a)
    
