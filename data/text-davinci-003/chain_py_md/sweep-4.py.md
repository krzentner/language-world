

Here is the code to perform the `sweep` task:

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper at the side of the cube
    #  2. Grab cube with the gripper
    #  3. Slide cube sideways to the goal
    
    # First, put the gripper to the side of the cube.
    if check("the robot's gripper is not horizontally aligned with the cube"):
        robot.move("gripper to the side of the cube")
    # Once the gripper is near the cube, grab it.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.grab("cube")
    # Now that the gripper is closed, we can slide the cube towards the goal.
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.slide("cube to the goal")
```