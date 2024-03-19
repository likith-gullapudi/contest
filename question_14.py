class Solution:
    def singleNumber(self, arr: List[int]) -> int:

        temp = [0 for i in range(32)]

        for i in arr:
            if i < 0:
                i = ~i + 1
            for j in range(32):
                temp[j] += 1 if ((i >> j) & 1) else 0

        ans2 = 0
        print(temp)
        for i in range(31):
            ans2 += ((temp[i] % 3) << i)
        ans2 -= 2 ** 31 if temp[31] == 1 else 0

        return ans2