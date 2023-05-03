
    if check("the robot's gripper is not vertically aligned with block"):
        robot.align("gripper to block")
    if check("the block is not left of the gripper and the gripper is not in front of the block"):
        robot.grab("block")
    if check("the robot's gripper is forward aligned with block and the robot's gripper is open"):
        robot.close("gripper on block")
    if check("the robot's gripper is closed around the block"):
        robot.place("block at goal")