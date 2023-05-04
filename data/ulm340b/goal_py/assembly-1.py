
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Slide the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the wrench is not left of the robot's gripper and the wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not almost horizontally aligned with the peg"):
        robot.move_gripper("above the wrench")
    # If the wrench is lined up with the peg, insert it.
    if check("the wrench is almost horizontally aligned with the peg"):
        robot.move_gripper("around the wrench", close_gripper=True)

# peg-unplug-side: slide the peg out of the hole to the left
def peg_unplug_side(robot):
    # Steps:
    #  1. Put the robot's gripper in front of the peg
    #  2. Slide the peg out to the right
    # If the gripper isn't in front of the peg, move it in front of the peg.
    if check("the robot's gripper is not in front of the peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # Once the gripper is lined up with the peg, we can push the peg out of the
    # hole.
    if check("the robot's gripper is horizontally aligned with the peg"):
        robot.move_gripper("right of the peg")

