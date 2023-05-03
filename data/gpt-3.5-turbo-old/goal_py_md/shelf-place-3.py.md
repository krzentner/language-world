# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Pick up block
    #  3. Move gripper to target location
    #  4. Place block at target location
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block, pick up the block.
    if check("the robot's gripper is around block and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location and open, move the gripper to
    # the target location.
    if check("the robot's gripper is above the target location" and "the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=False)
        robot.move_gripper("above the target location")
    # If the gripper is above the target location and closed, place the block at
    # the target location.
    if check("the robot's gripper is above the target location" and "the robot's gripper is closed"):
        robot.move_gripper("near the target location", close_gripper=False)