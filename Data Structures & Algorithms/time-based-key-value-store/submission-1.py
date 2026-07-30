class TimeMap:
    def __init__(self):
        self.times = []
        self.maps = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times.append(timestamp)
        self.maps[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.times) - 1
        time = -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == timestamp:
                time = mid
                break
            elif self.times[mid] < timestamp:
                time = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if time == -1:
            return ""
        
        for i in range(time, -1, -1):
            if key in self.maps[self.times[i]]:
                return self.maps[self.times[i]][key]
        
        return ""
