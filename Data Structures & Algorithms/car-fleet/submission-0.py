class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        out = 1
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(reverse=True)

        prevtime = (target - cars[0][0]) / (1.0 * cars[0][1])
        for i in range(1, n):
            curtime = (target - cars[i][0]) / (1.0 * cars[i][1])
            if curtime <= prevtime:
                continue
            
            else:
                prevtime = curtime
                out += 1
        
        return out