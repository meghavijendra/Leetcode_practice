import math
from typing import List


def findNumbers(self, nums: List[int]) -> int:
    res = 0
    for i in nums:
        leng = math.floor(math.log10(i))+1
        if (leng % 2 == 0 and i > 9):
            res += 1
    return(res)


def main():
    nums = [555, 901, 4822, 1771]
    res = findNumbers(0, nums)
    print(res)


if __name__ == "__main__":
    main()
