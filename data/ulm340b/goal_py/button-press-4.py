
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # Because this is a "front" button press, we just need to line up the gripper
    # from the front.
    # If the gripper is not aligned with the button as seen from the front, move
    # it into alignment.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is almost vertically aligned with the button and the robot's gripper is open"):
        robot.move_gripper("around the button")

# peg-insert: grab the peg and insert it into the hole
def peg_insert(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg, and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is around the peg and the peg is not vertically aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole, insert it.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("vertically aligned with