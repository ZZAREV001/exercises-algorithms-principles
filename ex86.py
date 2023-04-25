# Maze paths (dynamic programming approach that solves the problem from sub-problem solution)
def path_through_maze(maze):   # maze is a matrix
    paths = [[0] * len(maze[0]) for _ in range(len(maze))]
    paths[0][0] = 1   # path matrix is initialized

    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1 or (i == 0 and j == 0):
                continue

            leftPaths = 0
            topPaths = 0
            if i > 0:
                leftPaths = paths[i - 1][j]
            if j > 0:
                topPaths = paths[i][j - 1]
            paths[i][j] = leftPaths + topPaths
    print(paths)   # display paths that we compute
    return paths[-1][-1]


print(path_through_maze([[0, 1, 0],
                         [0, 0, 1],
                         [0, 0, 0]]))   # a 2 dimensions matrix

