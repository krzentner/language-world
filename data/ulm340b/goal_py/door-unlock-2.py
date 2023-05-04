
    # Steps:
    #  1. Put gripper above door dial
    #  2. Grab the door dial with the gripper
    #  3. Turn the door dial to unlock the door
    # First, put the gripper mostly above the door dial.
    if check("the robot's gripper is not vertically aligned with door dial"):
        robot.move_gripper("vertically aligned with the door dial", close_gripper=True)
    # As long as the gripper is roughly lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with door dial and the robot's gripper is open"):
        robot.move_gripper("around the door dial")
    # Now that the gripper is around the door dial, we can just turn it.
    if check("the robot's gripper is around door dial"):
        robot.move_gripper("around the door dial")

# peg-insert-side-goal-side: grab the peg and insert it into the hole
def peg_insert_side_goal_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is