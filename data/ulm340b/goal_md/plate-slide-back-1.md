

The task `plate-slide-forward` requires the robot to slide the plate out of the target location.
To slide the plate out of the target location reliably, what steps the robot should perform?

The task `bottle-open` requires the robot to open the cap off the bottle.
To open the cap off the bottle reliably, what steps the robot should perform?

The task `window-slide-open` requires the robot to slide the window open.
To slide the window open reliably, what steps the robot should perform?

The task `bottle-cap-remove` requires the robot to remove the cap from the bottle.
To remove the cap from the bottle reliably, what steps the robot should perform?

The task `cap-place` requires the robot to grab the cap and place it in the target location.
To grab the cap and place it in the target location reliably, what steps the robot should perform?

The task `plate-slide-side` requires the robot to slide the plate to the target location.
To slide the plate to the target location reliably, what steps the robot should perform?

'''
[eod] [code]"""
1219. Path with Maximum Gold
Easy

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position you can walk one step to the left, right, up or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.



Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 