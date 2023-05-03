

The bin-picking task requires the robot to pick up a cube and place it in the target bin. Here's the steps for completing the task:

1. Put the gripper above the cube
2. Drop the gripper around the cube
3. Close the gripper around the cube
4. Move the gripper up, transporting the cube
5. Move the gripper towards the target bin
6. Release the cube into the target bin

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Move gripper up, transporting the cube
    #  5. Move gripper towards the target bin
    #  6. Release cube into the target bin
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube up, transporting it.
    # If we didn't grab it, we'll just go back to a earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("gripper up, transporting the cube")
    # Move the gripper towards the target bin.
    if check("the robot's gripper is not near target bin"):
        robot.move("gripper towards the target bin")
    # Release the cube into the target bin.
    if check("the robot's gripper is above the cube and the robot's gripper is closed and the gripper is near the target bin"):
        robot.release("cube into the target bin")
```