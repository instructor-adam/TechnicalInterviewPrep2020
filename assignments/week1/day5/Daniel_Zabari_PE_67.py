# Assuming the triangle file is named accordingly...
with open("p067_triangle.txt") as file_:
    text = file_.read()
lines = text.split('\n')
triangle = [line.split() for line in lines]
triangle.pop()
traversal_dict = {}
row_length = len(triangle)

# Memoization technique:
def traverse_down(row, col):
    if row >= row_length:
        return 0
    if (row, col) in traversal_dict:
        return traversal_dict[(row, col)]
    num = int(triangle[row][col])
    left = traverse_down(row+1, col) + num
    right = traverse_down(row+1, col+1) + num
    if left > right:
        traversal_dict[(row, col)] = left
        return left
    traversal_dict[(row, col)] = right
    return right

print(traverse_down(0, 0))

# Tabulation technique:
def max_from_bottom():
    last_row = [int(num) for num in triangle[-1]]
    for i in range(len(triangle)-2, -1, -1):
        row = triangle[i]
        for j in range(0, len(row)):
            row[j] = max(last_row[j], last_row[j+1]) + int(row[j])
        last_row = triangle[i]
    return triangle[0][0]

print(max_from_bottom())


# Also can start at top and select max in each row, not max number,
# but max path based on previous values, this will give you 1000 values at the
# end then just select max.
