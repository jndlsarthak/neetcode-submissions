class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        start_pos = [(0,0) , (0,3), (0,6),
                     (3,0) , (3,3), (3,6),
                     (6,0) , (6,3), (6,6)]
        
        # Checking 3x3 boxes
        for i_start, j_start in start_pos:
            s = set()

            for i in range(i_start, i_start + 3):
                for j in range(j_start, j_start + 3):
                    num = board[i][j]

                    if num != '.':
                        if num in s:
                            return False
                        else:
                            s.add(num)

        # Checkig rows
        for i in range(9):
            s = set()

            for j in range(9):
                num = board[i][j]

                if num != '.':
                    if num in s:
                        return False
                    else:
                        s.add(num)

        # Checking columns
        for j in range(9):
            s = set()

            for i in range(9):
                num = board[i][j]

                if num != '.':
                    if num in s:
                        return False
                    else:
                        s.add(num)

        return True
                
