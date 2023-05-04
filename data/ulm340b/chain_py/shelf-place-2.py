
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move gripper above target
    #  5. Drop block
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # Since the block is large and flat, we should move the gripper roughly above
    # where we want the block to be placed instead of trying to place it very
    # exactly.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("gripper above target")
    # If the block is still around the gripper, it's time to release it.
    if check("the robot's gripper is above target and block is around the robot's gripper"):
        robot.drop("block")

# stack: grab a block from a stack and place it in another stack
def stack(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block above target
    #  5. Drop block onto target
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
