# Last updated: 7/10/2025, 2:09:11 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        hash_columns = []

        for i, row in enumerate(grid):
            temp_col = []
            for j, _ in enumerate(row):
                temp_col.append(grid[j][i])
            hash_columns.append(hash(tuple(temp_col)))

        for _, r in enumerate(grid):
            row = hash(tuple(r))
            for _, c in enumerate(hash_columns):
                if row == c:
                    result += 1

        return result