class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, nums):
        n=len(nums)
        prefix_even=[0 for i in range(n)]
        prefix_odd=[0 for i in range(n)]
        sufix_even=[0 for i in range(n)]
        sufix_odd=[0 for i in range(n)]
        even=odd=0
        for i in range(n):
            prefix_even[i]=even
            prefix_odd[i]=odd
            if i%2==0:
                even+=nums[i]
            else:
                odd+=nums[i]
        even=odd=0
        for i in range(n-1,-1,-1):
            sufix_even[i]=even
            sufix_odd[i]=odd
            if i%2==0:
                even+=nums[i]
            else:
                odd+=nums[i]
        ans=0
        for i in range(n):
            if prefix_even[i]+sufix_odd[i]==prefix_odd[i]+sufix_even[i]:
                ans+=1
        return ans