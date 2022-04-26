'''
剑指offer第5题：替换空格
'''

class Solution(object):
    # 方法1：原地交换——时间复杂度O(N)，空间复杂度O(1)
    def replaceSpace(self, s):
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else:
                res.append(i)
        return ''.join(res)

if __name__ == '__main__':
    s = "We are happy."
    sl = Solution()
    res = sl.replaceSpace(s)
    print(res)

