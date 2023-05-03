# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Lift the peg
    #  4. Move the gripper to the side of the hole
    #  5. Lower the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Once the gripper is above the peg, we can grab it by moving the gripper down
    # around it.
    if check("the robot's gripper is above the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper is around the peg, we can lift it up.
    if check("the robot's gripper is around the peg and the peg is not lifted up"):
        robot.lift_item()
    # Once the peg is lifted, we can move the gripper to the side of the hole.
    if check("the peg is lifted up and the robot's gripper is not moved to the side of the hole"):
        robot.move_gripper("side of the hole")
    # Once the gripper is to the side of the hole, we can move it down to insert
    # the peg into the hole.
    if check("the robot's gripper is to the side of the hole and the peg is not inserted"):
        robot.move_gripper("into the hole", close_gripper=True)