class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        flag = False
        def search(memory: List[Tuple[int, int]]):
            nonlocal flag
            mln = len(memory)
            wln = len(word)
            if mln == wln:
                flag = True
                return
            
            i = memory[-1][0]
            j = memory[-1][1]
            #move to:

            #up
            if 0 <= i-1 < len(board) and board[i-1][j] == word[mln] and (i-1,j) not in memory:
                search(memory + [(i-1,j)])

            #down
            if 0 <= i+1 < len(board) and board[i+1][j] == word[mln] and (i+1,j) not in memory:
                search(memory + [(i+1,j)])

            #left
            if 0 <= j-1 < len(board[0]) and board[i][j-1] == word[mln] and (i,j-1) not in memory:
                search(memory + [(i,j-1)])

            #right
            if 0 <= j+1 < len(board[0]) and board[i][j+1] == word[mln] and (i,j+1) not in memory:
                search(memory + [(i,j+1)])


        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    search([(i, j)])
                    if flag:
                        return True
        return False
