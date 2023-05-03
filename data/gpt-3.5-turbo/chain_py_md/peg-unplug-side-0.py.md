# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the plug
    #  4. Move the peg out of the plug
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the plug, line up the peg with the plug.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with plug"):
        robot.align("peg to plug")
    # If the peg is lined up with the plug to the side, unplug it.
    if check("peg is horizontally aligned with plug"):
        robot.pull("peg out of plug")