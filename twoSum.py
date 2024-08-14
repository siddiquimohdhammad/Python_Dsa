# arr = [1, 2, 3, 10]
# t = 5
# found =False
# # hm={}
# for i in range(len(arr)):
    
#     for j in range(i+1,len(arr)):
#         sum=arr[i]+arr[j]
#         if sum==t:
#             print(arr[i],arr[j])
#             found=True

# # print(sum)
# if found:
#     print("y")
# else:
#     print("no")
    

arr=[1,2,3,4,5]
t=30

found=False

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        curr_sum=arr[i]+arr[j]

        if curr_sum==t:
            print(i,j)
            found=True

if found:
    print("found")
else:
    print("not found")



