# Steps:
    #  1. Put the gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Lift the box lid off the box
    #  4. Move the gripper above the box
    #  5. Place the box lid on the box
    # First, put the gripper above the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper is not around the box lid, grab the box lid
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # If the gripper has the box lid, lift it up
    if check("the robot's gripper is around the box lid and the box lid is not lifted up"):
        robot.move_gripper("above the box")
    # If the gripper is above the box, place the box lid on the box
    if check("the robot's gripper is above the box and the box lid is lifted up"):
        robot.move_gripper("on the box")