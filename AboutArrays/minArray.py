'''
剑指offer第11题：旋转数组的最小数字
'''

class Solution(object):
    # 二分法，时间复杂度O(logN)，空间复杂度O(1)
    def minArray(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return min(nums[left: right])
        return nums[left]

if __name__ == '__main__':
    nums1 = [3, 4, 5, 1, 2]
    nums2 = [2, 2, 2, 0, 1]
    s = Solution()
    print(s.minArray(nums1))
    print(s.minArray(nums2))