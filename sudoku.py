

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Each dictionary represents the number of occurrences of elements in a row

        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]  # The elements of each row are stored in a dictionary, the key is a number, and the value is uniformly 1.
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        # Only traverse the entire board once
        # It can be inferred which 3*3 grid this point is in by i, j
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3 * (i // 3) + (j // 3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3 * (i // 3) + (j // 3)][num] = 1  # Divide the matrix into nine blocks
                else:
                    return False

        return True
