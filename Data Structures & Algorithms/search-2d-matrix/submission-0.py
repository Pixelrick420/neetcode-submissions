class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            
            elif matrix[mid][-1] < target:
                left = mid + 1
            
            else:
                row = matrix[mid]
                print(row)
                low = 0
                high = len(matrix[0]) - 1

                while low <= high:
                    mid = (low + high) // 2

                    if row[mid] > target:
                        high = mid - 1
                    
                    elif row[mid] < target:
                        low = mid + 1
                    
                    else:
                        return True

                return False

        return False