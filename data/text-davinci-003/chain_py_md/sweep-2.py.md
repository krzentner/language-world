

The code:

```
# sweep: grab the cube and move sideways it to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move cube sideways to desired location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube sideways to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("cube to the target")
```