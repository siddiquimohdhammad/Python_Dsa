'''
# x=['a','b','c','d','e']

# for i in x:
#     print(i,end=" ")
n=5
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("=================================================================")

# for i in range(n):
#     for j in range(n,i,-1):
#         print(j,end=" ")
#     print()


for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
# p=1
# q=10
# for i in range(p,q+1,2):
#     print(i)
'''
# max of array
array=[1,31,4,5]
n=len(array)

max=array[0]

for i in range(1,n):
    if array[i]>max:
        max=array[i]

print("max is ",max)

# check if array is sorted or not
def check(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            print("not Sorted")
            return 
    print(" Sorted")

check([1,2,30,4])

# for i in range(len(array)):
#     if array[i]<array[i+1]:
#         print("not")
    # print("sorted")

# swap variables
a=10
b=4
a,b=b,a
print(a)
# tuple unpacking
cont=("a","b","ikesdhf")
(z,x,m)=cont

print(m)

# reverse list
def reverseList(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    print(arr)
        

reverseList([1,2,3,4,5],0,4)

# kth smallest from array

def ksmall(a,k):
    a.sort()
    print(a[k])

ksmall([45,23,4521,45,154],4)

