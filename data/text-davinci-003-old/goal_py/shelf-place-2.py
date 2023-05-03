
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Carry block to goal
    # Put the gripper roughly above the block so that we don't accidentally bump
    # it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around it.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block, close the gripper.
    if check("the robot's gripper is near the block and the block is below the robot's gripper"):
        robot.move_gripper("above the target location")