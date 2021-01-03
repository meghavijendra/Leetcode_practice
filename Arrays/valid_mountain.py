from typing import List


def validMountainArray(self, A: List[int]) -> bool:
    if len(A) > 2:
        ind = A.index(max(A))
        low = A[:ind+1]
        high = A[ind:]
        if len(high) < 2 or len(low) < 2:
            return False
        i, j = 0, 0
        while(i < len(low)-1 and low[i] < low[i+1]):
            i += 1
        while(j < len(high)-1 and high[j] > high[j+1]):
            j += 1
        if i+j == len(A)-1:
            return True


def main():
    nums = [1, 2, 3, 5, 3, 0]
    res = validMountainArray(0, nums)
    print(res)


if __name__ == "__main__":
    main()
