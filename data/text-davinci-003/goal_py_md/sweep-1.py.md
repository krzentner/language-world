

Solution:

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Move gripper with cube towards the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, start sliding it towards the target
    # location.
    if check("the robot's gripper is around cube"):
        robot.move_gripper("near the target location")
```