

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper near the block, so that we can get a grip on it.
    if check("the robot's gripper is not near the block"):
        robot.put("gripper above block")
    # If the block is lined up with the gripper but still has a bit of space
    # between them, put the gripper around the block.
    if check("the robot's gripper is not around block and the robot's gripper is forward aligned with block"):
        robot.drop("gripper around block")
    # If the gripper is near the block, try to close it around the block to get
    # a better grip.
    if check("the robot's gripper is near block and the robot's gripper is not closed"):
        robot.close("gripper around block")
    # Now that the gripper is closed and the block is held firmly, we can
    # move the block to the goal.
    if check("the robot's gripper is closed and the block is secure"):
        robot.move("block to goal")