class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mid = sum(nums) / 2
        if mid != int(mid):
            return False
        mid = int(mid)
        dp = []
        temp = [False] * (mid + 1)
        if nums[0] < len(temp):
            temp[nums[0]] = True

        dp.append(temp)

        for i in range(1, len(nums)):
            tmp = dp[-1].copy()
            turn = dp[-1].copy()

            for j in range(len(tmp)):
                if tmp[j] is True and j + nums[i] < len(tmp):
                    turn[j + nums[i]] = True

            if nums[i] < len(tmp):
                turn[nums[i]] = True

            if turn[-1]:
                return True
            dp.append(turn)
        return False
