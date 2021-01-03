from typing import List


def checkIfExist(self, arr: List[int]) -> bool:
    i = 0
    j = 0
    d = {}
    a = arr.count(0)
    if a == 2:
        return True
    res = None
    for i, v in enumerate(arr):
        d[v] = i
    for v, k in d.items():
        if v % 2 == 0:
            g = v/2
            if g in d and d[v] != d[g]:
                return True


def main():
    nums = [7, 1, 14, 11]
    res = checkIfExist(0, nums)
    print(res)


if __name__ == "__main__":
    main()
