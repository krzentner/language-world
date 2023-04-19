
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Drop the gripper around the box lid
    #  3. Pick up the box lid by closing the gripper
    #  4. Place the box lid on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # Once the lid is on the box, open the gripper to let go of the lid.
    if check("the robot's gripper is above the box"):
        robot.move_gripper("above the box lid", close_gripper=False)