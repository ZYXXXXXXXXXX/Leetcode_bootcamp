class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for items in nums:
            if items not in hashmap:
                hashmap[items]=1
            else:
                hashmap[items]+=1
        fre_max=1
        for keys,v in hashmap.items():
            fre_max=max(fre_max,v)
        
        arr=[[] for _ in range(fre_max)]

        for keys,v in hashmap.items():
            arr[v-1].append(keys)
        
        res=[]
        i=len(arr)
        while len(res)<k:
            res+=arr[i-1]
            i-=1
        return res
