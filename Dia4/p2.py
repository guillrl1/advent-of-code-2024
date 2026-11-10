class Solution:
    def part1(self, data):
        lines = data[:]
        lines.extend(["".join([row[i] for row in data]) for i in range(len(data[0]))])

        def find_diagonals(grid):
            rows, cols = len(grid), len(grid[0])

            # from top-left to bottom-right
            main_diagonals = {}

            # from top-right to bottom-left
            anti_diagonals = {}

            for r in range(rows):
                for c in range(cols):
                    key_main = r - c
                    if key_main not in main_diagonals:
                        main_diagonals[key_main] = []
                    main_diagonals[key_main].append(grid[r][c])

                    key_anti = r + c
                    if key_anti not in anti_diagonals:
                        anti_diagonals[key_anti] = []
                    anti_diagonals[key_anti].append(grid[r][c])

            return main_diagonals, anti_diagonals

        main_diagonals, anti_diagonals = find_diagonals(data)
        lines.extend(["".join(i) for i in main_diagonals.values()])
        lines.extend(["".join(i) for i in anti_diagonals.values()])

        return sum(line.count("XMAS") + line.count("SAMX") for line in lines)

    def part2(self, data):
        rows, cols = len(data), len(data[0])
        count = 0

        _set = {"M", "S"}

        # find A as center of the cross, then check the diagonals
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if data[r][c] == "A":
                    if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                        count += 1

        return count

# Leer el archivo 'pingo.txt' y procesar los datos
def read_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

# Ruta al archivo pingo.txt
file_path = "pingo.txt"

try:
    # Leer el archivo y procesar con la solución
    data = read_file(file_path)
    solution = Solution()
    result_part2 = solution.part2(data)
    print(f"El resultado de la Parte 2 es: {result_part2}")
except FileNotFoundError:
    print(f"El archivo '{file_path}' no se encuentra.")
