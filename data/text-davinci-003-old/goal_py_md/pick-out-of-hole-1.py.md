

Steps:
1. Move the gripper slightly above the hole
2. Lower the gripper into the hole, making sure to grip the peg at the top
3. Move the gripper back up, still holding onto the peg
4. Move the gripper to the target location

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
#def pick_out_of_hole(robot):
    # Steps:
    #  1. Move the gripper slightly above the hole
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    #  2. Lower the gripper into the hole, making sure to grip the peg at the top
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("into the hole")
    #  3. Move the gripper back up, still holding onto the peg
    if check("the robot's gripper is in the hole and the robot's gripper is open"):
        robot.move_gripper("upwards", close_gripper=True)
    #  4. Move the gripper to the target location
    if check("the robot's gripper is upwards and the peg is held in the gripper"):
        robot.move_gripper("at the target location")
```