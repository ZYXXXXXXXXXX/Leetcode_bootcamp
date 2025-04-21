class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ptr_set={}
        pts=[0]*numCourses
        for items in prerequisites:
            pts[items[0]]+=1

            if items[1] not in ptr_set:
                ptr_set[items[1]]=[items[0]]
            else:
                ptr_set[items[1]].append(items[0])

        que=[]
        for i in range(numCourses):
            if pts[i]==0:
                que.append(i)
        if len(que)==0:
            return []
        res=[]
        visited=set([])
        
        while len(que)>0:
            num=len(que)
            for i in range(num):
                # i learn the class
                res.append(que[i])
                visited.add(que[i])
                # minus pts
                if que[i] not in ptr_set:
                    continue
                else:
                    for items in ptr_set[que[i]]:
                        pts[items]-=1
            del que[0:num]
            
            # add new ones
            for i in range(numCourses):
                if pts[i]==0 and i not in visited:
                    que.append(i)
            
        if len(res)!=numCourses:
            return []
            
        return res
