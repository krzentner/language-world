```
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper near the lid
    #  2. Grab the lid with the gripper
    #  3. Move gripper to the top of the box
    #  4. Place lid on top of the box
    # First, put the gripper near the lid.
    if check("the robot's gripper is not near the lid"):
        robot.move_gripper("near the lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around lid and the robot's gripper is open"):
        robot.move_gripper("around the lid", close_gripper=True)
    # If the lid is grabbed, move the gripper to the top of the box.
    if check("the robot's gripper is around the lid and the robot's gripper is not vertically aligned with the top of the box"):
        robot.move_gripper("vertically aligned with the top of the box")
    # Place the lid on top of the box.
    if check("the robot's gripper is vertically aligned with the top of the box and the robot's gripper is around the lid"):
        robot.move_gripper("above the box")