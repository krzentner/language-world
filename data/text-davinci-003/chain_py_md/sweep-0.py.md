

The program should look like the following:

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Slide the cube sideways to the goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the cube is not left of the gripper, go back to putting the gripper above the cube.
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.grab("cube")
    # Once the gripper is around the cube, try to slide it to the goal.
    if check("the robot's gripper is forward aligned with the cube"):
        robot.slide("cube to goal")
```