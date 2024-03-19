class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        zero = 0
        for i in nums:
            if i != 0:
                pro *= i
            else:
                zero += 1
        ans = []
        if zero > 1:
            return [0 for i in range(len(nums))]
        elif zero == 1:
            for i in nums:
                if i == 0:
                    ans.append(pro)
                else:
                    ans.append(0)
            return ans
        else:

            for i in nums:
                ans.append(pro // i)
            # print(ans)
            return ans

