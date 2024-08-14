# arr=[100,24,30,4,5]
# def check(arr):

#     for i in range(len(arr)):
#         if arr[i]<arr[i-1]:
#             return "sorted"
#         else:
#             return "not sorted"
        
# sor=check(arr)
# print(sor)


# selection sort
arr=[15,1,3,4,5,4,18,10]
def sortNum(arr):
    for i in range(len(arr)-1):
        min=i
        print(min)
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min=j

        # arr[i],arr[min]=arr[min],arr[i]
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

sortNum(arr)        

# print(arr)