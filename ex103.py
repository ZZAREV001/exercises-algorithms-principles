# Maximum connected colors in a grid (presence of a color is represented by 1 and 0 if no color present)
class Grid:   # 2D array data structure for representing colors (get / set colors etc.)
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        max_n = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                max_n = max(max_n, self.dfs_iterative(x, y, {}))   # pass the empty hashmap inside depth-first search function
        return max_n

    def neighbors(self, x, y):
        POSITIONS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = []
        for pos in POSITIONS:
            if self.colorAt(x + pos[0], y + pos[1]) == self.colorAt(x, y):
                n.append((x + pos[0], y + pos[1]))
        return n

    def dfs(self, x, y, visited):    # recursive approach of depth-first search algorithm
        key = str(x) + ', ' + str(y)
        if key in visited:
            return 0
        visited[key] = True
        result = 1
        for neighbor in self.neighbors(x, y):
            result += self.dfs(neighbor[0], neighbor[1], visited)
        return result

    def dfs_iterative(self, x, y, visited):  # iterative approach of depth-first search algorithm
        stack = [(x, y)]
        result = 0
        while len(stack) > 0:
            (x, y) = stack.pop()
            key = str(x) + ', ' + str(y)
            if key in visited:
                continue
            visited[key] = True

            result += 1
            for neighbor in self.neighbors(x, y):
                stack.append(neighbor)

        return result

    def colorAt(self, x, y):
        if x >= 0 and x < len(self.grid[0]) \
                and y >= 0 and y < len(self.grid):
            return self.grid[y][x]
        return -1


grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
# expected 7 (there are 7 connected colors in the grid input.

