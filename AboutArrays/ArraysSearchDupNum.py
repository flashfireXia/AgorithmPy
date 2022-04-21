'''
剑指offer第3题：数组中的重复数字
'''

class Solution(object):
    # 方法1：原地交换——时间复杂度O(N)，空间复杂度O(1)
    def findRepeatNumber(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

    # 方法2：哈希表——时间复杂度O(N)，空间复杂度O(N)*/
    def findRepeatNumber2(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
        return -1

if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    res = s.findRepeatNumber(nums)
    print(res)