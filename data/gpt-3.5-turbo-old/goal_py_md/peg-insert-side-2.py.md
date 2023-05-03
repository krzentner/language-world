# peg-insert-side: insert the peg into the hole from the side
# def peg_insert_side(robot):
# First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg isn't to the left of the gripper, move the gripper to the left
    # of the peg.
    if check("peg is not left of the robot's gripper"):
        robot.move_gripper("left of the peg")
    # If the gripper is not around the peg and the gripper is open, move the
    # gripper around the peg and close it to grab onto the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Once we've grabbed the peg, move it towards the hole until it is roughly
    # lined up.
    if check("the robot's gripper is around the peg and the peg is not roughly horizontally aligned with hole"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Slide the peg into the hole.
    if check("the robot's gripper is horizontally aligned with hole and the peg is roughly horizontally aligned with the hole"):
        robot.move_gripper("horizontally aligned with hole")