

Steps: 
1. Put gripper above the basketball
2. Drop gripper around basketball 
3. Move the basketball towards the hoop
4. Release the basketball into the hoop

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the basketball
    #  2. Drop gripper around basketball 
    #  3. Move the basketball towards the hoop
    #  4. Release the basketball into the hoop
    # First, put the gripper above the basketball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the basketball"):
        robot.move_gripper("above the basketball")
     # If the gripper isn't around the basketball, put it around the basketball.
    if check("the robot's gripper is not around basketball and the robot's gripper is open"):
        robot.move_gripper("near the basketball", close_gripper=True)
     # If the gripper is near the basketball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above basketball and the robot's gripper is closed"):
        robot.move_gripper("towards the hoop")
    # Once the robot has the basketball in its grip, move it to the hoop and
    # release it.
    if check("the robot's gripper is near the hoop"):
        robot.move_gripper("above the hoop", release=True)