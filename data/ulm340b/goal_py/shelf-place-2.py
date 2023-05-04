
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("above the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("above the target location")

# handoff: pick up the block and place it in the cup
def handoff(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to top of cup
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("above the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("above the cup")

# stacking: move the block from the floor onto the tower block
def stacking(robot):
