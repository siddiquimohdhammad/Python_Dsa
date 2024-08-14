def fibo(n):
    a=0
    b=1

    if n==1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n):
            sum=a+b
            a=b
            b=sum
            print(sum)

# fibo(5)

arr=[12,56,1,2,0]
# arr.sort()
# print("==>",arr)
print(len(arr))
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
