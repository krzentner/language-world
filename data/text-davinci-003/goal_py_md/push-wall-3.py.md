

Here's the program for `push-wall`:

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above and left of puck
    #  2. Push gripper down and right to trap puck between gripper and wall
    #  3. Slide trapped puck to goal
    # First, move the gripper left and above the puck, so that it can fit
    # between the puck and the wall.
    if check("the robot's gripper is not above and left of the puck"):
        robot.move_gripper("above and left of the puck")
    # Once the gripper is in the right spot, push down and right to trap the
    # puck between the gripper and the wall.
    if check("the robot's gripper is above and left of the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")
    # If the puck is now trapped between the gripper and the wall, we should be
    # able to slide it to the target.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the target location")
```