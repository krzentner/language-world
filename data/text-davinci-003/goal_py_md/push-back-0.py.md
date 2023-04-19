

The robot's code should look like this:

```
# push-back: slide the puck backwards to the target location
# def push_back(robot):    
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # We need to put the gripper roughly above the puck before we can start to
    # push it back.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Now that the gripper is roughly above the puck, we can try to push the
    # puck back by trapping it from above. We want the gripper to be roughly
    # around the puck.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the gripper is around the puck, just move it above the target
    # location. This should slide the puck back to the target location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the target location")
```