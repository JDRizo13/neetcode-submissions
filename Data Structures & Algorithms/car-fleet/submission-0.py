class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1 and len(speed) == 1:
            return 1 
        cars = []

        for i in range(len(position)):
            pos = position[i]
            spd = speed[i]
            cars.append((pos, spd))

        cars.sort(reverse=True)
        slowestTime = 0 
        counter = 0 
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > slowestTime:
                counter += 1
                slowestTime = time
        return counter