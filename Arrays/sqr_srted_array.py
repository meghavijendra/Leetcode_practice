from typing import List


def sortedSquares(self, A: List[int]) -> List[int]:
    for i, v in enumerate(A):
        v = abs(v)
        A[i] = v * v
    A.sort()
    return (A)


def main():
    nums = [-4, -1, 0, 3, 10]
    res = sortedSquares(0, nums)
    print(res)


if __name__ == "__main__":
    main()
