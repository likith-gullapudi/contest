class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        ans=float('inf')
        s=0
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                ans=min(ans,r-l+1)
                s-=nums[l]
                l+=1
            r+=1
        return ans if ans!=float('inf') else 0