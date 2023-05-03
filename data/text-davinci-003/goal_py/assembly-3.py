
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line up the wrench with the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is horizontally or backward aligned with the gripper, the
    # gripper is probably behind it and can just slide it into position.
    if check("the wrench is horizontally aligned with the robot's gripper and the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Otherwise, the gripper is probably around the wrench, so we can just slide
    # the wrench into the correct position.
    if check("the wrench is left of the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the peg")

# switch-light: open the switch and turn on the light
def switch_light(robot):
    # Steps:
    #  1. Put gripper above the switch
    #  2. Flip the switch open
    # If the gripper isn't above the switch, the robot needs to move to the
    # switch to flip it open.
    if check("the robot's gripper is not above the switch"):
        robot.move_gripper("above the switch")
    # Once the robot's gripper is above the switch, open it.
    if check("the robot's gripper is above the switch"):
        robot.move_gripper("horizontally aligned with the switch", close_gripper=True)