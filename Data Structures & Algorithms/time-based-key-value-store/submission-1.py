class TimeMap:

    def __init__(self):
        self.timemap: dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = list()
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        times = self.timemap[key]
        left = 0
        right = len(times) - 1
        res = ""
        while left <= right:
            i = left + ((right - left) // 2)
            if timestamp > times[i][0]:
                res = times[i][1]
                left = i + 1
            elif timestamp < times[i][0]:
                right = i - 1
            else:
                return times[i][1]
        return res