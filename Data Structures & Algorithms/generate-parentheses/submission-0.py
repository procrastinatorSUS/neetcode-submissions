class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        substr = ''
        def dfs( op: int, cl: int):
            nonlocal substr
            

            if op == cl == n:
                res.append(substr)
                return
            
            if op != n:
                substr += '('
                dfs(op+1, cl)
                substr  = substr[:-1]
            
            if op > cl:
                substr += ')'
                dfs(op, cl+1)
                substr  = substr[:-1]
        dfs(0, 0)
        return res