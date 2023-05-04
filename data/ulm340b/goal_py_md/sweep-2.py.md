

### Overview

The robot's goal in the sweep task is to take the cube to the target location.

The robot starts with its gripper near the cube. The robot's gripper should not touch the cube while moving to its open position to avoid accidentally knocking the cube out of place.

Once the robot's gripper is near the cube, it can grab the cube by closing the gripper, but be careful not to touch the cube while the gripper is closed.

Once the robot's gripper is closed, the cube is held by the robot.

When the robot's gripper is holding the cube, the robot can move the cube to the target location. However, the robot can't move the cube through the walls, so you'll need to pick a different route.

When the robot's gripper is close to the target location and holding the cube, you're done!

Here's a full example program of how you could get the robot to sweep:

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Move gripper above the cube
    #  2. Close gripper
    #  3. Navigate to target location
    # Move the robot's gripper out of the way of the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Now that the gripper is out of the way, just close it to grab the cube.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Navigate the robot to the target location while avoiding obstacles
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target location")
```

'''

# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Move gripper above the cube
    #  2. Close gripper
    #  3. Navigate to target location
    # Move the robot's gripper out of the way of the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Now that the gripper is out of the way, just close