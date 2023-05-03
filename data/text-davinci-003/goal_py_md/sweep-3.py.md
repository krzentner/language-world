

Here's the program: 

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around cube
    #  4. Move cube sideways to target location
    # First, put the gripper roughly above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the cube")
    # If the cube is close enough, grab it and move it sideways to the target
    # location.
    if check("the robot's gripper is vertical aligned with cube and the cube is not in front of the target location"):
        robot.move_gripper("horizontally aligned with the target location") 
```