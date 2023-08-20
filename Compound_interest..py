rate=float(input("Please enter the rate: "))
principal=int(input("Please enter the principal: "))
time=int(input("Please enter the time: "))
Amount=principal

for i in range(time):
        Amount = Amount * (1 + rate)
        CI = Amount - principal
        print("Compound interest is", CI)
        

