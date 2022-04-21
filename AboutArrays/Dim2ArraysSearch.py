'''
剑指offer第4题：二维数组中的查找
'''

class Solution(object):
    # 从右上角(当然也可以是左下角)查找，遇到目标值小于当前值则左移列，目标值大于当前值则下移行，若相等，返回True
    # 时间复杂度O(M + N)，空间复杂度O(1)
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    target1 = 11
    target2 = 0
    s = Solution()
    print(s.findNumberIn2DArray(matrix, target1))
    print(s.findNumberIn2DArray(matrix, target2))
