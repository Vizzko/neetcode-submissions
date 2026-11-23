class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Piece 2: the range of possible speeds
        low = 1
        high = max(piles)

        # Piece 1: does this speed finish in time?
        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += pile // k          # full hours
                if pile % k != 0:           # leftover bananas
                    hours += 1              # one extra hour
            return hours <= h

        # Piece 3: binary search on the speed
        while low < high:
            mid = (low + high) // 2

            if can_finish(mid):
                high = mid                  # works, so try slower (keep mid)
            else:
                low = mid + 1               # too slow, so go faster

        return low


        