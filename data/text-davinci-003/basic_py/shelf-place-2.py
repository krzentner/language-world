
    if check("the robot's gripper is not near the block"):
        robot.move("gripper to near the block")
    if check("the robot's gripper is near the block and the robot's gripper is open"):
        robot.close("gripper around the block") 
    if check("the robot's gripper is closed and the block is not near the target location"):
        robot.move("block to target")
    if check("the block is near the target location and the robot's gripper is closed"):
        robot.release("block at target")