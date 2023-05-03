

The stick pull program should do the following steps:

1. Put gripper above the stick
2. Grab the stick with the gripper
3. Place the end of the stick at the thermos
4. Pull the thermos towards the target location

```
# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):    
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Place the end of the stick at the thermos
    #  4. Pull the thermos towards the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not near stick"):
        robot.move_gripper("above the stick")
    # If the stick isn't below the gripper as seen from above, move the gripper
    # above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Once the gripper is above the stick, we can grab the stick by closing the
    # gripper.
    if check("the robot's gripper is above the stick and the robot's gripper is open"):
        robot.move_gripper("above the stick", close_gripper=True)
    # We need to place the end of the stick at the thermos, so first move the
    # gripper to the end of the stick.
    if check("the robot's gripper is not at the bottom of the stick and the robot's gripper is near the stick"):
        robot.move_gripper("at the bottom of the stick")
    # Once the gripper is at the end of the stick, we should be able to slide it
    # under the thermos.
    if check("the robot's gripper is at the bottom of the stick and the thermos is not below the stick"):
        robot.move_gripper("below the thermos")
    # Once the end of the stick is under the thermos, the robot can pull the
    # thermos towards the target location.
    if check("the robot's gripper is below the thermos and the robot's gripper is near the target location"):
        robot.move_gripper("near the target location")
```