
class Solution:

    def isPossible(self, S):
        d={}
        for i in S:
            d[i]=(d.get(i,0)+1)%2
        temp=1 if len(S)%2==1 else 0
        for i in d.values():
            if i!=0:
                if temp==0:
                    return False
                else:
                    temp-=1
        return True
