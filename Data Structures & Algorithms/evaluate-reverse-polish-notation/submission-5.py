class Solution:


    def is_num(self, s:str) -> bool:
        if s[0] in '+-':
            return len(s) > 1 and s[1:].isdigit()
        else:
            return s.isdigit()


    def evalRPN(self, tokens: List[str]) -> int:
        dig_list = []
        last = ''
        for token in tokens:
            if self.is_num(token):
                dig_list.append(token)
            else:

                rez = int(eval(f'{dig_list[-2]}{token}{dig_list[-1]}'))
                dig_list.pop()
                dig_list.pop()
                dig_list.append(rez)
        return int(dig_list[0]) 
