arr=[11,2,3,4,5,1]
# 2 3 4 5 1

n=len(arr)


temp=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
    
arr[n-1]=temp

print(arr)