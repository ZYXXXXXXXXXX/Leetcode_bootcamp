class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        if amount<=0:
            return 0
        dp=[]
        temp = [float('inf')] * (amount + 1)
        temp[0] = 0
        i=1
        while i*coins[0]<=amount:
            temp[i*coins[0]]=i
            i+=1
        dp.append(temp)

        for j in range(1,len(coins)):
            tmp=dp[-1].copy()
            this_turn=dp[-1].copy()

            l=1
            while l*coins[j]<=amount:
                tmp[l*coins[j]]=min(l,tmp[l*coins[j]])
                this_turn[l*coins[j]]=min(l,this_turn[l*coins[j]])
                l+=1
            
            for k in range(len(tmp)):
                if tmp[k]!=0 and k+coins[j]<len(tmp):
                    this_turn[k+coins[j]]=min(this_turn[k]+1,this_turn[k+coins[j]])

            dp.append(this_turn)

        if dp[-1][-1] == float('inf'):
            return -1
        return dp[-1][-1]    
