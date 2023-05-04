
    # Steps:
    #  1. Put the robot's gripper near the puck
    #  2. Push the puck
    # Move the robot's gripper near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # Push the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("above the target location")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # First, put the gripper roughly around the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("above door handle", close_gripper=True)
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with door handle")
[eod] [code]from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < heightMap.__len__() and 0 <= dy < heightMap[0].__len__() and (
                        dx, dy) not in visited and heightMap[dx][dy] != 0:
                    dfs(dx, dy)

        for x, row in enumerate(heightMap):
            for y, h in enumerate(row):
                if h != 0:
                    dfs(x, y)

        return sum(sum(map(max, (heightMap[y][x] for x in range(y, 0, -