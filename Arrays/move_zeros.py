from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    temp = nums.count(0)
    i = 0
    while i < (len(nums)-temp):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i += 1
    return nums


def main():
    nums = [7, 0, 0, 1, 14, 11]
    res = moveZeroes(0, nums)
    print(res)


if __name__ == "__main__":
    main()
