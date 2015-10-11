class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        lenRow = len(board)
        if lenRow <= 0:
        	return
        lenCol = len(board[0])
        if lenCol <= 0:
        	return

        for n in lenRow:
        	for m in lenCol:
        		if n - 1 >= 0 and m - 1>= 0:
        			neighbor0 = board[n-1][m-1]
        		else:
        			neighbor0 = 0

        		if n - 1 >= 0:
        			neighbor1 = board[n-1][m]
        		else:
        			neighbor1 = 0

        		if n - 1 >= 0 and m + 1 < lenCol 
        			neighbor2 = board[n-1][m+1]
        		else:
        			neighbor2 = 0

        		if m + 1 < lenCol:
        			neighbor3 = board[n][m+1]
        		else:
        			neighbor3 = 0

        		if n + 1 < lenRow and m + 1 < lenCol:
        			neighbor4 = board[n+1][m+1]
        		else:
        			neighbor4 = 0

        		if n + 1 < lenRow:
        			neighbor5 = board[n+1][m]
        		else:
        			neighbor5 = 0

        		if n + 1 < lenRow and m - 1 >= 0:
        			neighbor6 = board[n+1][m-1]
        		else:
        			neighbor6 = 0

        		if m - 1 >= 0:
        			neighbor7 = board[n][m-1]
        		else:
        			neighbor7 = 0

        		board[n][m] = nextState(board[n][m], neighbor0, neighbor1, neighbor2, neighbor3, neighbor4, neighbor5, neighbor6, neighbor7)

        for n in lenRow:
        	for m in lenCol:
        		board[n][m] = board[n][m] >> 1