def count_xmas_occurrences(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    word = "XMAS"
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Directions for searching: (row_offset, col_offset)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Down-Right (Diagonal)
        (1, -1),  # Down-Left (Diagonal)
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Up-Left (Diagonal)
        (-1, 1)   # Up-Right (Diagonal)
    ]

    def search(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[k]:
                return 0
        return 1

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                count += search(i, j, dx, dy)

    return count

# Run the function on the input file
filename = "pingo.txt"
print(count_xmas_occurrences(filename))
