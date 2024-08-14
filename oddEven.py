# n=11
# a=[1,2,3,4,5,6,56,14,78,55]
# l=[]
# for i in range(len(a)):
#     if a[i]%2!=0:
#         l.append(a[i])
# print(l)


# if 10%n==0:
#     print("even")
# else:
#     print("odd")

n=6
flag=False

if n==1:
    print("not a PN")
elif n>1:

    for i in range(2,n):
       if n%i==0:
            flag=True 
            break

if flag:
    print("not a pn")
else:
    print("pn")