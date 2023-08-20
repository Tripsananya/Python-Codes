name=input("Enter your Name: ")
marks=int(input("Enter your Marks: "))

if(marks>90):
    print("Grade A..")
elif(marks>=80 and marks>=70):
    print("Grade B..")
elif(marks>=70 and marks>=60):
    print("Grade c..")
elif(marks>=60 and marks>=50):
    print("Grade D..")
elif(marks>=50 and marks>=40):
    print("Grade E..")
else:
    print("Fail..")
