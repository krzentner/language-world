# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg upwards and out of the hole
    #  4. Move the gripper to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is aligned with the peg but not around it, put it around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the peg is not inside the gripper"):
        robot.move_gripper("around the peg")
    # If the gripper is around the peg, lift the peg upwards out of the hole.
    if check("the robot's gripper is around the peg and the peg is inside the gripper"):
        robot.move_gripper("almost vertically aligned with the peg")
    # Once the peg is almost lifted out of the hole, move the gripper to the target location.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("above the target location")