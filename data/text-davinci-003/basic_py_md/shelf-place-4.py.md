

if check("the robot's gripper is not near the block"):
    robot.reach("to block")
if check("the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block"):
    robot.put("the gripper above the block")
if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not near the block"):
    robot.drop("the gripper around the block")
if check("the robot's gripper is around the block and the block is below the robot's gripper"):
    robot.lift("block off shelf")
if check("the robots gripper is near the block and the block is above the robots gripper"):
    robot.place("block at destination")