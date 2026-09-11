# ======================================
# LeetCode Problem: surrounded regions
# Language: python
# Link: https://leetcode.com/problems/surrounded-regions/
# Synced by: LinkCode
# Date: 9/11/2026, 6:33:09 PM
# ======================================


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"