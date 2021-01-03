from typing import List


def heightChecker(self, heights: List[int]) -> int:
    count = 0
    leng = len(heights)
    srt = sorted(heights)
    for i in range(leng):
        if heights[i] != srt[i]:
            count += 1
        i += 1
    return count


def main():
    nums = [1, 4, 3, 8, 4, 1]
    res = heightChecker(0, nums)
    print(res)


if __name__ == "__main__":
    main()
