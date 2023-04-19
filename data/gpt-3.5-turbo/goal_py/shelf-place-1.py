# Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Lift the block up
    #  4. Move the block to the target location
    #  5. Lower the block down
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block and closed, lift the block up.
    if check("the robot's gripper is around block and the robot's gripper is not near the shelf"):
        robot.move_gripper("above the shelf")
    # If the gripper is above the shelf, move it to the target location.
    if check("the robot's gripper is above the shelf and the robot's gripper is not almost vertically aligned with the target location"):
        robot.move_gripper("almost vertically aligned with the target location")
    # Once the gripper is almost vertically aligned with the target location,
    # lower the block down.
    if check("the robot's gripper is almost vertically aligned with the target location"):
        robot.move_gripper("above the target location")