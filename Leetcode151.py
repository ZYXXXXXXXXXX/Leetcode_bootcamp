class Solution:
    def reverseWords(self, s: str) -> str:
        arr1=s.split()
        arr2=[]
        for i in range(len(arr1)-1,-1,-1):
            arr2.append(arr1[i])
        return ' '.join(arr2)
