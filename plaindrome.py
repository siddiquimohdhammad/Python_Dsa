'''
a="mom"
# print(len(a))
# print(a[0])
# pal=a[::-1]

pal=[]
for i in range(len(a)-1,-1,-1):
    pal.append(a[i])
    
# print(pal)
    
    
pal_string=''.join(pal)

if pal_string==a:
    print("It is palindrom")
else:
    print("Not a plaindrome")
'''

# a="mom"

# pal=[]
# for i in range(len(a)-1,-1,-1):
#     pal.append(a[i])

# pal_string=''.join(pal)

# if pal_string==a:
#     print("palindrome")
# else:
#     print("not pal")

a='mom'

l=[]

for i in range(len(a)-1,-1,-1):
    l.append(a[i])

pal_str=''.join(l)

if pal_str==a:
    print("y")
else:
    print("no")