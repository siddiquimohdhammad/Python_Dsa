nums=[1,0,2,2,33,33,4,4]

count=nums[0]

for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[count]=nums[i]
        print("======>",nums[count])
        count+=1
nums = nums[:count]

print(nums)