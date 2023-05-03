
    if check("the robot's gripper is not above block and the robot's gripper is not vertically aligned with the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not near block"):
        robot.push("the gripper into the block")
    if check("the robot's gripper is near the block"):
        robot.drop("the block on the shelf")
    if check("the block is not resting on the shelf"):
        robot.place("the block on the shelf")