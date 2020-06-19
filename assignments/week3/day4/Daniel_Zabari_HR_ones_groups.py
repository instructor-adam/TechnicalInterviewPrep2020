import collections

def onesGroups(grid, queries):
    island_stack = []
    max_row = len(grid)
    max_col = len(grid[0])
    check_row = 0
    check_col = 0
    size_dict = collections.defaultdict(int)
    while check_row < max_row:
        check_col = 0
        while check_col < max_col:
            print(check_row, check_col)
            if grid[check_row][check_col] == 1:
                island_stack.append((check_row, check_col))
                size = 0
                while island_stack != []:
                    point = island_stack.pop()
                    if (
                        (point[0] < 0) or
                        (point[0] >= max_row) or
                        (point[1] < 0) or
                        (point[1] >= max_col)
                       ):
                        continue
                    if grid[point[0]][point[1]] == 1:
                        size += 1
                        grid[point[0]][point[1]] = -1
                        island_stack.append((point[0]+1, point[1]))
                        island_stack.append((point[0]-1, point[1]))
                        island_stack.append((point[0], point[1]+1))
                        island_stack.append((point[0], point[1]-1))
                        print(size)
                size_dict[size] += 1
            check_col += 1
        check_row += 1
    answer = []
    for query in queries:
        answer.append(size_dict[query])
    return answer
