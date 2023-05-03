
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # Put robot gripper above block.
    if check("the robot's gripper is not above block or the robot's gripper is not vertically aligned with the block"):
        robot.move_gripper("vertically aligned with the block", close_gripper=True)
    # If the block is below the gripper and the gripper is open, grab the block.
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is open"):
        robot.move_gripper("above the block")
    # If the block is held in the gripper, place it on the shelf at the target
    # location.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("near the target location")