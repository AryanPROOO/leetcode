class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        row = [""] * numRows
        current_row = 0
        direction = 1
        for char in s:
            row[current_row] += char
            if current_row == numRows - 1:
                direction = -1
            elif current_row == 0:
                direction = 1
            current_row += direction
        return "".join(row)