from typing import List


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    leng = 0
    for i, v in enumerate(nums):
        if v == 1:
            leng += 1
            nums[i] = leng
        else:
            leng = 0
    res = max(nums)
    return (res)


def main():
    nums = [1, 1, 0, 1, 1, 1]
    res = findMaxConsecutiveOnes(0, nums)
    print(res)


if __name__ == "__main__":
    main()
