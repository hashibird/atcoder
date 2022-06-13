n = int(input())
a_list = list(map(int, input().split()))


nums = [i for i in range(0, 2001)]

for a in a_list:
    if a in nums:
        nums.remove(a)
print(nums[0])