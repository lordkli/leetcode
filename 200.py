from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rowNumber = len(grid)
        columnNumber = len(grid[0])
        visited = set()
        islandCounter = 0
        
        def bfs(row, column):
            myQueue = []
            visited.add((row, column))
            myQueue.append((row, column))
            
            while len(myQueue) != 0:
                row, column = myQueue.pop(0)
                myDirections = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for rowDirection, columnDirection in myDirections:
                    newRow = row + rowDirection
                    newColumn = column + columnDirection
                    
                    if(newRow in range(rowNumber) and
                      newColumn in range(columnNumber) and
                       grid[newRow][newColumn] == "1" and
                       (newRow, newColumn) not in visited):
                        visited.add((newRow, newColumn))
                        myQueue.append((newRow, newColumn))
        
        for row in range(rowNumber):
            for column in range(columnNumber):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    islandCounter += 1
        
        return islandCounter
    
    
    
    # 2
    class Solution:
        def _checkIsland(self, grid: List[List[str]], i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return False

            if grid[i][j] == '0':
                return False
            if grid[i][j] == '-1':
                return False
            grid[i][j] = '-1'
            self._checkIsland(grid, i+1, j)
            self._checkIsland(grid, i-1, j)
            self._checkIsland(grid, i, j-1)
            self._checkIsland(grid, i, j+1)
            return True
            

        def numIslands(self, grid: List[List[str]]) -> int:
            island_count: int = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if self._checkIsland(grid, i, j):
                        island_count += 1
            return island_count