class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rez = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack:
                while stack and  temperatures[stack[-1]] < temperatures[i]:
                    rez[stack[-1]] = i-stack[-1]
                    stack.pop()
                stack.append(i)
            
            else:
                stack.append(i)
        return rez