
    # Steps:
    #  1. Put gripper above the shelf and aligned with the block to pick it up
    #  2. Drop the gripper around the block
    #  3. Move the block to the goal
    # First, put the gripper above the shelf, so that we don't bump it while
    # trying to grab the block.
    if check("the robot's gripper is not above shelf"):
        robot.put("gripper above shelf")
    # If the gripper isn't aligned with the block, align it.
    if check("the robot's gripper is not horizontally aligned with block"):
        robot.align("gripper to block")
    # If the gripper is aligned, start dropping it around the block.
    if check("the robot's gripper is horizontally aligned with block and the gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is around the block, move it to the goal.
    if check("the robot's gripper is around block"):
        robot.place("block at goal")