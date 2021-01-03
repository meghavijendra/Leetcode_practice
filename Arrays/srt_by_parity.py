from typing import List


def sortArrayByParity(self, A: List[int]) -> List[int]:
    leng = len(A)
    i, loop = 0, 0
    while(loop != leng):
        if A[i] % 2 != 0:
            A.append(A[i])
            A.pop(i)
        else:
            i = i+1
        loop += 1
    return (A)


def main():
    nums = [7, 0, 0, 1, 14, 11]
    res = sortArrayByParity(0, nums)
    print(res)


if __name__ == "__main__":
    main()
