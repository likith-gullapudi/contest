import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and math.log(n, 3) == int(math.log(n, 3))