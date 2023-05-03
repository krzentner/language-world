

The program should complete the following steps:

1. Put the gripper above the cube
2. Drop the gripper around the cube
3. Close the gripper around the cube
4. Move the cube to the target location

Solution:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, we can probably grab it by closing the
    # gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")