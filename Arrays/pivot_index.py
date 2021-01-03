from typing import List


def pivotIndex(self, nums: List[int]) -> int:
    leng = len(nums)
    if leng > 3:
        leftsum = 0
        rightsum = sum(nums)
        for i, v in enumerate(nums):
            rightsum -= v
            if leftsum == rightsum:
                return i
            leftsum += v
        return -1
    else:
        return -1


def main():
    nums = [1, 7, 3, 6, 5, 6]
    res = pivotIndex(0, nums)
    print(res)


if __name__ == "__main__":
    main()
