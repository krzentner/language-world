

Steps:
1. Put gripper above basketball
2. Drop gripper around basketball
3. Close gripper around basketball
4. Move the basketball to the hoop
5. Hoop the basketball

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above basketball
    #  2. Drop gripper around basketball
    #  3. Close gripper around basketball
    #  4. Move the basketball to the hoop
    #  5. Hoop the basketball
    # First, put the gripper above the basketball.
    if check("the robot's gripper is not above the basketball"):
        robot.place("gripper above basketball")
    # If the gripper isn't around the basketball, put it around the basketball.
    if check("the robot's gripper is not around basketball and the robot's gripper is open"):
        robot.drop("gripper around basketball")
    # If the gripper is near the basketball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near basketball and the robot's gripper is open"):
        robot.close("gripper around basketball")
    # We closed the gripper, and the basketball is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the basketball to the hoop.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above basketball and the robot's gripper is closed"):
        robot.move("basketball to hoop")
    # If the basketball is near the hoop, complete the task. Hoop the basketball.
    if check("the basketball is near the hoop"):
        robot.hoop("basketball")