

Then the program:

```
# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # 
    # The robot can slide the puck by trapping it by pushing down on it from
    # behind and moving the gripper.
    # If the puck isn't to the left of the gripper as seen from behind, move the
    # gripper to the left of the puck.
    if check("the robot's gripper is not left of puck and the robot's gripper is not perpendicular to the puck"):
        robot.put("the gripper left of the puck")
    # If the gripper is perpendicular to the puck but not near it, move the
    # gripper downward to the puck to slide it.
    if check("the robot's gripper is perpendicular to the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is left of the robot's gripper"):
        robot.slide("the puck to the goal") 
```