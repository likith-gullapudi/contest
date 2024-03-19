"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def count(self, head, key):
        temp = head
        ans = 0
        while temp:
            if temp.data == key:
                ans += 1
            temp = temp.next

        return ans