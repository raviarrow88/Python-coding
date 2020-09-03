# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1= l1
        s2=l2

        d1= ''
        d2=''
        while s1:
            d1 += str(s1.val)
            s1 = s1.next


        while s2:
            d2 += str(s2.val)
            s2 = s2.next

        s1_rev = d1[::-1]
        s2_rev = d2[::-1]

        s1_sum = int(s1_rev)
        s2_sum = int(s2_rev)

        total = str(s1_sum + s2_sum)

        res = (total[::-1])

        return map(int,list(res))
