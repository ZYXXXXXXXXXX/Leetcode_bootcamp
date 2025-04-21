class Solution:
    def rotting(self, grid, m, n):
        if (
            (0 <= m + 1 < len(grid))
            and (0 <= n < len(grid[0]))
            and grid[m + 1][n] == 1
        ):
            grid[m + 1][n] = 2
            self.que.append([m + 1, n])
        if (
            (0 <= m - 1 < len(grid))
            and (0 <= n < len(grid[0]))
            and grid[m - 1][n] == 1
        ):
            grid[m - 1][n] = 2
            self.que.append([m - 1, n])
        if (
            (0 <= m < len(grid))
            and (0 <= n + 1 < len(grid[0]))
            and grid[m][n + 1] == 1
        ):
            grid[m][n + 1] = 2
            self.que.append([m, n + 1])
        if (
            (0 <= m < len(grid))
            and (0 <= n - 1 < len(grid[0]))
            and grid[m][n - 1] == 1
        ):
            grid[m][n - 1] = 2
            self.que.append([m, n - 1])
        return


    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        self.que = []
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.que.append([i, j])
                if grid[i][j] ==1:
                    count+=1

        if count==0:
            return 0
        if len(self.que) == 0:
            return -1


        
        while len(self.que) > 0:
            print(self.que)
            num = len(self.que)
            for i in range(num):
                self.rotting(grid, self.que[i][0], self.que[i][1])
            del self.que[0:num]
            time += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time-1
