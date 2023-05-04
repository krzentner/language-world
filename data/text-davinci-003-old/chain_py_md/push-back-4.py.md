

The program should be as follows:

```
# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper into back of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # behind and moving the gripper.
    # If the puck isn't behind the gripper as seen from behind, move the
    # gripper to behind the puck.
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper behind the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # back to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is behind the robot's gripper"):
        robot.slide("the puck to the goal")
```