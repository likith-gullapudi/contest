class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=ans=right=0
        dic=dict()
        while right<len(s):
            dic[s[right]]=dic.get(s[right],0)+1
            while len(dic)<right-left+1:# dic[s[right]]==2:
                #print(dic,left,right)
                dic[s[left]]-=1
                if dic[s[left]]==0:
                    del dic[s[left]]
                left+=1
            right+=1
            ans=max(ans,right-left)

        return ans