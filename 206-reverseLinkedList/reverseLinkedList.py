#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 递归
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            # 返回子链表的反转链表
            reversed_sub_list = self.reverseList(head.next)
            # 将子链表的反转链表的最后一个节点指向第一个节点
            head.next.next = head
            # 原链表的第一个节点变为反转链表的最后一个节点,next置为None,否则遍历链表时找不到结束节点next == None
            head.next = None

            return reversed_sub_list

    # 迭代
    def reverseListIteration(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        first_node = head

        current_node = head
        next_node = current_node.next
        while True:
            if next_node != None:
                # 将下一个节点保存在临时变量中
                tmp = next_node.next

                next_node.next = current_node
                current_node = next_node

                if tmp == None:
                    first_node.next = None
                    return next_node
                next_node = tmp
