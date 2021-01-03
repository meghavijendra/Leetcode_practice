from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    while(i < len(nums)):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return (len(nums))


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    res = removeElement(0, nums, val)
    print(res)


if __name__ == "__main__":
    main()
