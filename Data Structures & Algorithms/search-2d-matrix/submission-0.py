class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        m = len(matrix)
        n = len(matrix[0])
        while i < m:
            if target >= matrix[i][0] and target <= matrix[i][n - 1]:
                break
            i += 1
        if i == m: return False

        l = 0
        r = n - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target == matrix[i][mid] : return True
            elif target > matrix[i][mid] : l = mid + 1
            elif target < matrix[i][mid] : r = mid - 1
        
        return False
        