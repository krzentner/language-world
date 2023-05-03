# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Rotate the wrist to face the hole
    #  5. Move the gripper forward to insert the peg into the hole
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Rotate the wrist to face the hole
    if check("the robot's wrist is not facing the hole"):
        robot.move_wrist("to face the hole")
    if check("the robot's wrist is facing the hole and the gripper is not at the hole"):
        robot.move_gripper("at the hole")