def list_sums(nums:list, sum:int):
    prefix_sums_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        prefix_sum = sum(nums[0:i+1])
        prefix_sums_dict[num] = prefix_sum

    print(prefix_sums_dict)
    







n = [2,3,5,-3,4,4,6,2]
print(list_sums(n, 5))
