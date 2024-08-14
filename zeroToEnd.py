arr=[1,0,2,0,4,0,5,64,0,0,0,12]

n=len(arr)
temp=[]

for i in range(n):
    if arr[i]!=0:
        temp.append(arr[i])

# print(temp)

for i in range(len(temp)):
    arr[i]=temp[i]

# print(arr)
# arr=[01203]
# 123__
for i in range(len(temp),n):
    arr[i]=0

print(arr)