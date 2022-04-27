'''
剑指offer第6题：从尾到头打印链表
'''

class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution(object):
    # 递归法，时间复杂度O(N)，空间复杂度O(N)
    def reversePrint1(self, head):
        if not head:
            return []
        return self.reversePrint1(head.next) + [head.val]

    # 栈，时间复杂度O(N)，空间复杂度O(N)
    def reversePrint2(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

if __name__ == '__main__':
    head = ListNode(1, ListNode(3, ListNode(2, ListNode(None, None))))
    s = Solution()
    print(s.reversePrint1(head))
    print(s.reversePrint2(head))
