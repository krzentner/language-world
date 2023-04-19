

Here's the program that performs the `sweep-into` task:

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Sweep around cube with gripper
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper above cube.
    if check("the robot's gripper is not near the cube"):
        robot.put("gripper above cube")
    # Sweep the gripper around the cube. This will ensure the robot can grab it
    # no matter which direction the cube is facing.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.sweep("gripper around cube")
    # Once the gripper is around the cube, close the gripper around it.
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # As long as the gripper is still around the cube, move the cube to the
    # target goal.
    if check("the robot's gripper is around cube"):
        robot.place("cube at goal")
```