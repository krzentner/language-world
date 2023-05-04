

The code needs to use a function named `check`.

There are lots of different ways to do the same thing.
I do not know what your code will look like.

Good luck!
"""

def disassemble(robot):
    if check("the peg is not vertically aligned with the robot's gripper"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not forward aligned with the peg and the peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the wrench is not vertically aligned with robot's gripper"):
        robot.align("wrench to robot's gripper")
    if check("the wrench is vertically aligned with robot's gripper"):
        robot.pull("wrench off the peg")

[eod] [code]""" 
Combinatorial

Given an array of distinct integers. The task is to count all the triplet
a, b, c such that a<b<c and a+b+c = 0.


Example 1:

Input:
N = 6
A[] = {-1, 0, 1, 2, -1, -4}
Output: 2
Explanation: There are two triplets with 
sum 0 
(-1, 0, 1) and (-1, -1, 2).

Your Task:
You don't need to read input or print anything. Your task is to complete 
the function countTriplet() which takes the array and its size as inputs 
and returns the number of such triplets.

"""


#User function Template for python3


def countTriplet(arr,n):
    triplets = 0
    hashMap = {}
    for i in range(n):
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1

    for i in range(n):
        # for triplet 0
        if (arr[i] * 2) in hashMap and hashMap[arr[i]*2] > 0:
            triplets += hashMap[arr[i]*2]
        # for triplet +ve sum
        elif (arr[i]*3) in hashMap and hashMap[arr[i]*3] > 0:
            triplets += hashMap[arr[i]*3]
        # for