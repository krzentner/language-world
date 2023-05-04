
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Slide the wrench down onto the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench is in front of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the wrench is not vertically aligned with the robot's gripper and the wrench is left of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the peg, line up the wrench with the peg.
    if check("the wrench is in front of the peg"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench is lined up with the peg, slide it down.
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not left of the robot's gripper"):
        robot.move_gripper("right of the peg")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg straight down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is not forward of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it