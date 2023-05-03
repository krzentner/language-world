# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the unplugging direction
    #  4. Pull the peg out from the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg, line up the peg with
    # the unplugging direction.
    if check("the robot's gripper is around the peg and the peg is not aligned with unplugging direction"):
        robot.move_gripper("aligned with the unplugging direction")
    # If the gripper is aligned with the unplugging direction and closed around
    # the peg, pull the peg out.
    if check("the robot's gripper is aligned with the unplugging direction and closed around the peg"):
        robot.move_gripper("above the peg and away from the hole")