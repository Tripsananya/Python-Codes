arr=[11,78,89,13,90]
n=len(arr)

for i in range(n-1):
    for j in range(0,n-i-2):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp     
print(arr)
        
        
