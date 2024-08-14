# second largest

arr=[15,45,12,100,2,2,2]
# 2 10 15 45 100
arr.sort()
n=len(arr)
l=arr[n-1]

for i in range(n-2,-1,-1):
    if arr[i]!=l:
        sl=arr[i]
        break
    
print(sl)


# second smallest
# arr[1,2,3,4]
smallest=arr[0]

for i in range(1,n):
    if arr[i]!=smallest:
        sm=arr[i]
        break

print(sm)