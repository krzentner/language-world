

Steps:
1. Put gripper above the box lid
2. Drop gripper around the box lid
3. Pick up the box lid
4. Move the box lid above the box
5. Place the box lid on the box 

```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put the gripper above the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    #  2. Drop the gripper around the box lid
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    #  3. Pick up the box lid
    if check("the robot's gripper is near the box lid"):
        robot.move_gripper("above the box lid")
    #  4. Move the box lid above the box
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("above the box")
    #  5. Place the box lid on the box
    if check("the robot's gripper is above the box"):
        robot.move_gripper("above the box lid")