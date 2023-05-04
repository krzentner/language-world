

After you write your program, press the "Done" button below to test it.
"""

# This is a stub, not a solution.
# You can use this directly by replacing text with what you want the robot to
# actually do, and checking if the check statement is true.


# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Go above the goal
    #  2. Move down onto the goal
    # Put gripper above goal.
    if check("the robot's gripper is not above goal"):
        robot.put("gripper above goal")
    # Put gripper at goal.
    if check("the robot's gripper is not near goal"):
        robot.put("gripper at goal")
[eod] [code]'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # TLE
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        last_val = node.val
        while node:
            next = node.next
            if next and next.val == node.val:
                node.next = node.next.next
            elif next and next.val != last_val:
                last_val = node.val
                node = node.next
            else:
                node = node.next
        return head


    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node:
            next = node.next
            if next and node.val == next.val:
                while node.next and node.val == next.val:
                    node.next = node.next.next
            else:
                node = node.next
        return head



def getnode(value):
    if not value:
        return None
   