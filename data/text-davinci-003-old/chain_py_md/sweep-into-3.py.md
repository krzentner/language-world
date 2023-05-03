

The code for `sweep-into` should look like this:

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put the gripper to the left of the cube
    #  2. Move the gripper in a sweeping motion to grab the cube
    #  3. Place the cube at the goal
    # Put the gripper to the left of the cube.
    if check("the robot's gripper is not to the left of the cube"):
        robot.move("gripper to left of cube")
    # Move the gripper in a sweeping motion starting to the left of the cube,
    # curving in to grab it.
    if check("the robot's gripper is not sweeping across the cube and the gripper is not near the cube"):
        robot.sweep("gripper towards cube")
    # If the gripper is near the cube and no longer sweeping, it's probably
    # caught the cube.
    # Close the gripper to make sure it holds the cube.
    if check("the robot's gripper is near the cube and the gripper is open"):
        robot.close("gripper around cube")
    # Move the held cube to the goal.
    if check("the robot's gripper is above the cube and the gripper is closed"):
        robot.sweep("cube to goal")
```