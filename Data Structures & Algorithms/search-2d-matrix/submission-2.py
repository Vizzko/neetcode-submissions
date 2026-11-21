class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                # target must be in this row if it exists, so binary search it
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False