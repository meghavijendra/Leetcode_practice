from typing import List


def removeDuplicates(self, nums):
    i = 0
    for num in nums:
        if num != nums[i]:
            i += 1
            nums[i] = num
    return i + 1


def main():
    nums = [7, 1, 1, 1, 14, 11]
    res = removeDuplicates(0, nums)
    print(res)


if __name__ == "__main__":
    main()
