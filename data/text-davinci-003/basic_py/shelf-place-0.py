
    if check("the robot's gripper is not above block"):
        robot.put("gripper above block")
    if check("the robot's gripper is open and the block is not right of the robot's gripper"):
        robot.grab("block")
    if check("the robot's gripper is not above target shelf"):
        robot.place("gripper above target shelf")
    if check("the robot's gripper is above target shelf and the block is not left of the robot's gripper"):
        robot.align("block to target shelf")
    if check("the block is left of the robot's gripper"):
        robot.drop("block on target shelf")