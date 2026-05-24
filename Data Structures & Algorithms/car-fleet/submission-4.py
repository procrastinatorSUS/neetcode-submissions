from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        rez = 0

        i = 0
        ln = (len(paired) - 1)
        while i <= ln:
            goal = (target - paired[i][0]) / paired[i][1]
            while i < ln and goal >= (target - paired[i+1][0])/paired[i+1][1]:
                i += 1
            rez += 1
            i += 1
        return rez