

# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps: 
    #  1. Put gripper above the box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around the box lid
    #  4. Move gripper with lid to the box
    #  5. Place lid on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is around the box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # Now that the box lid is in the gripper we can move it to the box.
    if check("the robot's gripper is above box"):
        robot.move_gripper("above the box lid", close_gripper=True)
    # Place the lid on the box.
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("around the box lid")