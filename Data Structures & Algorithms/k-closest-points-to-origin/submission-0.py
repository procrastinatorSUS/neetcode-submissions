class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dct = {}
        for x in points:
            dist = (x[0]**2 + x[1]**2)**0.5
            if dist not in dct:
                dct[dist] = [x]
            else:
                dct[dist].append(x)
        # dct = { (x[0]**2 + x[1]**2 )**0.5 : x for x in points}
        
        cords = list(dct.keys())
        heapq.heapify(cords)

        res = []
        while k != 0:
            cord = dct[heapq.heappop(cords)]
            for point in cord:
                if k != 0:
                    res.append(point)
                    k-=1
                else:
                    break
    

        return res
    