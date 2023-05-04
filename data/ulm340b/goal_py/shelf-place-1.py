
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around block
    #  3. Grab the block
    #  4. Place the block on the shelf
    # If the block is above the gripper as seen from the side, move the gripper
    # above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # As long as the gripper is aligned with the block, move the gripper down
    # until we can grab the block.
    if check("the robot's gripper is vertically aligned with the block"):
        robot.move_gripper("above the block", close_gripper=True)
    # If the block is around the robot's gripper, try to lift it.
    if check("the robot's gripper is vertically aligned with the block and the block is near the robot's gripper"):
        robot.move_gripper("vertically aligned with the target location")

# shelf-place-side: pick up the block and place it at the target location
def shelf_place_side(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around block
    #  3. Grab the block
    #  4. Place the block on the shelf
    # If the block is not above the gripper as seen from the side, move the
    # gripper above the block.
    if check("the robot's gripper is not almost vertically aligned with the block"):
        robot.move_gripper("almost vertically aligned with the block")
    # As long as the gripper is aligned with the block, move the gripper down
    # until we can grab the block.
    if check("the robot's gripper is almost vertically aligned with the block"):
        robot.move_gripper("almost above the block", close_gripper=True)
    # If the block is around the robot's gripper, try to lift it.
    if check("the robot's gripper is almost vertically aligned with the block and the block is below the robot's gripper"):
        robot.move_gripper("near the target location")

# shelf-place-back: pick