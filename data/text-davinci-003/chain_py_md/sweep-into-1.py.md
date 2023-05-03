

Using the same structure as the other programs, the code for `sweep-into` would look like this:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target
    #  First, put the gripper above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the cube is not to the left of the robot's gripper, grab it by moving
    # the gripper downward to the cube.
    if check("the cube is not left of the robot's gripper and the robot's gripper is not vertically aligned with the cube"):
        robot.grab("cube")
    # As long as the gripper is still around the cube (and the robot is not
    # near the goal), move the cube to the goal.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near target"):
        robot.sweep("cube to goal")
```