def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    leng = len(nums) + 1
    nums = list(set(nums))
    i = 1
    count = 0
    while(i != leng):
        if i not in nums:
            nums.append(i)
            count += 1
        i += 1
    if count != 0:
        return(nums[-count:])
    else:
        return []
