class Solution:
    def hasAlternatingBits(self, num: int) -> bool:
        binary_string = bin(num)[2:]
        for i in range(len(binary_string) - 1):
            if binary_string[i] == binary_string[i + 1]:
                return False
        return True
