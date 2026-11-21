class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        best = 0

        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1

            window_length = right - left + 1
            paint_needed = window_length - max(count.values())

            while paint_needed > k:
                count[s[left]] -= 1          # letter leaves the frame
                left += 1                    # frame start moves forward

                window_length = right - left + 1
                paint_needed = window_length - max(count.values())

            best = max(best, right - left + 1)   # note the valid window size

        return best