# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if None == l1:
            return l2

        if None == l2:
            return l1

        # use l1 as the result container
        result = l1
        # use 'cross' to avoid allocating new ListNode
        cross = False
        while None != l1 and None != l2:
            overflow = 0
            if not cross:
                l1.val += l2.val
            if l1.val >= 10:
                l1.val = l1.val % 10
                overflow = 1

            if overflow:
                if None != l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            elif None == l1.next and None != l2.next:
                l1.next = l2.next
                cross = True


            if None == l2.next and None != l1.next:
                l2.next = l1.next
                cross = True

            l1 = l1.next
            l2 = l2.next

        return result
