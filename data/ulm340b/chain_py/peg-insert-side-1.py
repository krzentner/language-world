
    # Steps:
    #  1. Put gripper around peg
    #  2. Move peg to hole
    # First, get the gripper roughly around the peg.
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # Now that we have the peg in the gripper, move it to the hole.
    if check("the robot's gripper is around peg and the peg is not near hole"):
        robot.place("peg in hole")

# peg-unstack-side: pick the top peg out of the stack by lifting it to the side
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper around peg
    #  2. Lift peg out of stack
    # First, get the gripper roughly around the peg.
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # Now that we have the peg in the gripper, move it out of the stack.
    if check("the robot's gripper is around peg and the peg is in the stack"):
        robot.lift("peg out of stack")

# peg-insert-side-only-one-peg: grab the peg and insert it into the hole from the side
def peg_insert_side_only_one_peg(robot):
    # Steps:
    #  1. Put gripper around peg
    #  2. Move peg to hole
    # First, get the gripper roughly around the peg.
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # Now that we have the peg in the gripper, move it to the hole.
    if check("the robot's gripper is around peg and the peg is not near hole"):
        robot.place("peg in hole")

# peg-unstack-side-only-one-peg: pick the top peg out of the stack by lifting it to the side
def peg_unstack_side_only_one_peg(robot):
    # Steps:
    #  1. Put gripper around peg
    #  2. Lift peg out of stack
    # First, get the gripper roughly around the peg.
    if check("the robot'