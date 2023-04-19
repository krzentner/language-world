
    # Steps:
    #  1. Reach the block
    #  2. Put gripper above block
    #  3. Drop gripper around block
    #  4. Close gripper around block
    #  5. Place the block on a shelf
    # First, reach towards the block.
    robot.reach("to block")
    # If the gripper is not above the block, then put the gripper above the
    # block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # Next, drop the gripper around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, close the gripper around the
    # block.
    if check("the robot's gripper is near the block and the robot's gripper is open"):
        robot.close("gripper around the block")
    # Next, move the block to the nearest shelf.
    if check("the robot is holding the block"):
        robot.place("block on shelf")