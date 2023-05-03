

The steps for `sweep` are:

1. Put gripper above cube.
2. Drop gripper around cube.
3. Close gripper around cube.
4. Move sideways with cube to target location.

```
# sweep: grab the cube and move sideways it to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move sideways with cube to target location
    # Place the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube, grasp it by closing the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We grasped the cube, now move it sideways to the target location.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("sideways with cube to target location")
```