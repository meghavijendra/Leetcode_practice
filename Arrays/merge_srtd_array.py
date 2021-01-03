from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(n):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()
    return (nums1)


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res = merge(0, nums1, m, nums2, n)
    print(res)


if __name__ == "__main__":
    main()
