class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        for i in range(1, num):
            if num % i == 0:
                s += i
        return s == num

