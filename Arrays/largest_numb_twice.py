from typing import List


def dominantIndex(self, nums: List[int]) -> int:
    if len(nums) >= 2:
        maxi = max(nums)
        ind = nums.index(maxi)
        nums.remove(maxi)
        maxi2 = max(nums)
        if maxi >= 2 * maxi2:
            return ind
        return -1
    else:
        return 0


def main():
    nums = [1, 3,  6]
    res = dominantIndex(0, nums)
    print(res)


if __name__ == "__main__":
    main()
