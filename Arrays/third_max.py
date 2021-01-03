from typing import List


def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums))
    srt = sorted(nums)
    leng = len(srt)
    if leng < 3:
        return srt[-1]
    else:
        return srt[-3]


def main():
    nums = [1, 4, 3, 8, 4, 1]
    res = thirdMax(0, nums)
    print(res)


if __name__ == "__main__":
    main()
