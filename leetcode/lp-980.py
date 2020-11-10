# 980. Unique Paths III
# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = sum(a == 0 for row in grid for a in row) # number of 0 grids to be travelled
        start = next((i, j) for i, row in enumerate(grid) for j, a in enumerate(row) if a == 1)
        end = next((i, j) for i, row in enumerate(grid) for j, a in enumerate(row) if a == 2)
        self.res = 0
        def backtrack(i, j, temp_count):
            grid[i][j] += 10
            if (i, j) == end and temp_count - 1 == count: # if reach the end and traveled all 0 grids
                self.res += 1
            if i > 0 and 0 <= grid[i - 1][j] < 5:                   backtrack(i - 1, j, temp_count + 1)
            if i < len(grid) - 1 and 0 <= grid[i + 1][j] < 5:       backtrack(i + 1, j, temp_count + 1)
            if j > 0 and 0 <= grid[i][j - 1] < 5:                   backtrack(i, j - 1, temp_count + 1)
            if j < len(grid[0]) - 1 and 0 <= grid[i][j + 1] < 5:    backtrack(i, j + 1, temp_count + 1)
            grid[i][j] -= 10

        backtrack(*start, 0)
        return self.res        
