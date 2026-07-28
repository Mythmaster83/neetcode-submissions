from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for g in range(9):
                val = board[i][g]

                if val == ".":
                    continue

                box_key = (i//3, g//3)

                if val in rows[i] or val in columns[g] or val in boxes[box_key]:
                    return False

                rows[i].add(val)
                columns[g].add(val)
                boxes[box_key].add(val)

        return True