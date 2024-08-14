# from pract import addValue

# arr=[45,21,45]
# a=addValue(arr,45)
# a=addValue(arr,45)
# a=addValue(arr,45)
# a=addValue(arr,45)
# print(a)

# from selction import sortNum

# arr=[15,45,87,6,4,0,2]
# sortNum(arr)
# print(arr)

# a="jfdklgjk"

# l=[]

# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])

# pal="".join(l)

# if a==pal:
#     print("y")
# else:
#     print('n')

# duplicates

a=[1,1,3,3,2,1,1,2,2,1,3,1,3,4,5,1]

# a.sort()

l=[a[0]]
seen={a[0]}
print(seen)

for i in range(1,len(a)):
    if a[i]!=a[i-1] and a[i] not in seen:
        l.append(a[i])
        seen.add(a[i])

print(l)
