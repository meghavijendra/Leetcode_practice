from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    res = sum(v * (10**i) for i, v in enumerate(digits[::-1])) + 1
    out = [int(d) for d in str(res)]
    return (out)
    

def main():
    nums = [1, 3,  6]
    res = plusOne(0, nums)
    print(res)


if __name__ == "__main__":
    main()
