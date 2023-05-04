
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close the gripper around the block
    #  4. Move the block above the target location
    #  5. Slide the block sideways to the goal
    # Put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.move_gripper("above the target location", open_gripper=True)
    # If the block is roughly vertically lined up with the target location but
    # not horizontally lined up with it, try to slide the block to it.
    if check("the robot's gripper is above the target location and the block is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location", open_gripper=True)

# shelf-pull: pull the block out to the start location
def shelf_pull(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close the gripper around the block
    #  4. Pull the block out
    # Put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open