
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block
    #  3. Place the block at the goal location
    # We need to  put the gripper above the block before grabbing it.
    if check("the robot's gripper is not above block and the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    # The gripper is above the block, so try to grab the block.
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is open"):
        robot.grab("block")
    # Argument: If the block is already in the gripper and the gripper is
    # closed, try to move the block to the goal location.
    if check("the block is in the robot's gripper and the robot's gripper is closed"):
        robot.move("block to goal")