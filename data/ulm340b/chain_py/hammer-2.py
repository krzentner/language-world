
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop gripper around hammer
    #  3. Pull hammer up
    #  4. Push hammer down on the nail
    # We need to put the gripper above the hammer before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with hammer"):
        robot.put("gripper above hammer")
    # Once the gripper is lined up above the hammer, we should be able to grab
    # the hammer by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with hammer and the robot's gripper is not around hammer"):
        robot.put("gripper around hammer")
    # Now that the gripper is around the hammer, pull the hammer up.
    if check("the robot's gripper is around hammer"):
        robot.pull("hammer up")
    # We've pulled the hammer up, so we should be able to push it back down on
    # the nail now.
    if check("the robot's gripper is around hammer"):
        robot.push("hammer down on nail")

# peg-unstack-side: push a peg off the side of a stack of pegs
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Push against the side of the top peg until it falls
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the top peg and the robot's gripper is below the top peg"):
        robot.put("gripper above the top peg")
    # As long as the robot's gripper is lined up with the top peg, push it over.
    if check("the robot's gripper is vertically aligned with the top peg"):
        robot.push("the top peg")

# peg-unstack-top: push a peg straight up off the top of a stack of pegs
def peg_unstack_top(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Push up on the top peg until it falls
    # First,