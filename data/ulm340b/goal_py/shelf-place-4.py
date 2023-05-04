
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move the block to the target location
    #  5. Put the block on the target location
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("near the target location", close_gripper=False)
    # If the gripper is vertically aligned with the block, drop the block on the
    # target location.
    if check("the robot's gripper is almost vertically aligned with the target location"):
        robot.move_gripper("below the target location", close_gripper=True)

# shelf-place-side: pick up the block sideways and place it at the target location
def shelf_place_side(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Line the block up with the target location
    #  4. Push the block down onto the target location
    # First, put the gripper above the block, so that we can easily grab it.
    if check("the robot's gripper is not vertically aligned with block"):
        robot.move_gripper("vertically aligned with the block")
    # If the block is still left of the gripper, go back to lining the gripper
    # up.
    if check("block is left of the robot's gripper"):
        robot.move_gripper("above block", close