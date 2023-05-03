

Here is the solution:

```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Drop gripper around dial on the door
    #  3. Turn the dial
    # Put the gripper to the right of the door handle so that it can reach the
    # dial.
    if check("the robot's gripper is not right of the door handle"):
        robot.move_gripper("right of the door handle")
    # Once the robot is at the dial, reach around it with the gripper to grab it.
    if check("the robot's gripper is right of the door handle and the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Turn the dial with the gripper.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("clockwise around the dial")
```