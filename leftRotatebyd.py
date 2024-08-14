arr=[1,2,3,4,5,6,7]
# 2 3 4 5 1

n=len(arr)
k=3
k=k%n
temp=[]
for i in range(k):

    # temp=arr[i]
    temp.append(arr[i])

# print(temp)


for i in range(k,n):
    arr[i-k]=arr[i]
    
# arr[n-1]=temp
j=0
for i in range(n-k,n):
    arr[i]=temp[j]
    j+=1

print(arr)