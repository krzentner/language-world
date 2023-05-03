

If check("the robot's gripper is not vertically aligned with the door handle"):
    robot.put("gripper above door handle")
if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not near door handle"):
    robot.move("gripper next to the door handle")
if check("the robot's gripper is near the door handle"):
    robot.rotate("dial on the door")