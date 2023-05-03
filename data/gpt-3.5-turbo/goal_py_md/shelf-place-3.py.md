# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move block to target location
    #  5. Open gripper to release the block
    # First, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # Move the gripper to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("around the block")
    # Open the gripper to release the block.
    if check("the robot's gripper is around the block"):
        robot.move_gripper("near the target location", open_gripper=True)