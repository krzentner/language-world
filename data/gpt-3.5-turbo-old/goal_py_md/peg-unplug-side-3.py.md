# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Tilt the peg out from the hole
    #  4. Pull the peg to the side
    #  5. Examine the peg to confirm that it's removed
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # If the gripper is mostly around the peg but the peg is still in the hole,
    # tilt the peg out of the hole by slightly opening the gripper and moving
    # the gripper to the side.
    if check("the robot's gripper is almost aligned with hole"):
        robot.move_gripper("left of the hole", close_gripper=False)
    # Once the gripper is to the side of the hole, pull the gripper away from
    # the hole to remove the peg.
    if check("the robot's gripper is left of the hole and the peg is not between the gripper claws"):
        robot.move_gripper("above the peg")
    # Finally, confirm that the peg has been removed by examining it.
    if check("the peg is still in the hole"):
        print("Peg removal failed, please retry")
    else:
        print("Peg successfully removed")