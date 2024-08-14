# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i,j,end=" ")

#     print()


# # other
# arr=[1,2,3,4,55]
# n=len(arr)

# max=arr[0]

# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]

# print("MAX is==>",max)
        
# arr.remove(arr[4])
# print(arr)

# list=[]

# for i in range(100):
#     # append.list(i)
#     list.append(i+1)

# print(list)

# n=[m for m in range(1,100+1) if m%2==0]
# print(n)

# array=[45,21,45,41,4]

# for i in array:
#     print(i,end=" ")

# print(" ")
def removeValue(arr,n):
    # return[j for j in arr if j!=n]
    list=[]
    for i in arr:
        if i!=n:
            list.append(i) 
    return list

    

arr=[1,2,3,445,454]
a=removeValue(arr,454)
# print(a)

def addValue(ar,val):
        ar+=[None]
        print(ar)
        ar[len(ar)-1]=val
        return ar
    

ar=[1,2,45]
arr=addValue(ar,855)
# arr=addValue(ar,84)
arr=addValue(ar,84)
# arr=addValue(ar,84)
# arr=addValue(ar,84)
print(arr)


