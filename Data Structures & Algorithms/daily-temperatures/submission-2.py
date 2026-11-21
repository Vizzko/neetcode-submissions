class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        waiting = []

        for today, temp in enumerate(temperatures):
            while waiting and temperatures[waiting[-1]] < temp:
                day = waiting.pop()
                result[day] = today - day
            waiting.append(today)

        return result
        