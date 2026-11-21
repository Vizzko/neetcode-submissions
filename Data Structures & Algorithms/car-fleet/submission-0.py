class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        checktime = 0
        cars = sorted(zip(position, speed), reverse=True)

        for pos, sped in cars:
            distance = target - pos
            time = distance / sped
            if time > checktime:
                fleet += 1
                checktime = time

        return fleet

                

        