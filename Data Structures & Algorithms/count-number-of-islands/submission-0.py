class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    count += 1
                    self.visit(grid, y, x)
        return count

    def visit(self, grid, y, x):
        if (
            0 <= y < len(grid) and 
            0 <= x < len(grid[y]) and 
            grid[y][x] == '1'
        ):
            grid[y][x] = '.'
            self.visit(grid, y - 1, x)
            self.visit(grid, y + 1, x)
            self.visit(grid, y, x - 1)
            self.visit(grid, y, x + 1)