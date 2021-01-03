from typing import List


def duplicateZeros(self, arr: List[int]) -> None:
    i = 0
    while(i < len(arr)):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1
    return (arr)


def main():
    nums = [1, 0, 2, 3, 0, 4, 5, 0]
    res = duplicateZeros(0, nums)
    print(res)


if __name__ == "__main__":
    main()
