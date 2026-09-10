# ======================================
# LeetCode Problem: surrounded regions
# Language: python
# Link: https://leetcode.com/problems/surrounded-regions/
# Synced by: LinkCode
# Date: 9/11/2026, 12:28:38 AM
# ======================================


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # Out of bounds or not an O
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != "O":
                return

            # Mark this O as safe
            board[r][c] = "#"

            # Up
            dfs(r - 1, c)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

            # Right
            dfs(r, c + 1)

        # 1. Start DFS from all border O's

        # Left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # 2. Flip surrounded O's
        # 3. Restore safe # back to O
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "#":
                    board[r][c] = "O"