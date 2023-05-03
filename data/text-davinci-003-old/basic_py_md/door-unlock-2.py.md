

If check("the robot's gripper is not vertically aligned with the keyhole"):
    robot.put("gripper above keyhole")
if check("the robot's gripper is vertically aligned with the keyhole"):
    robot.turn("dial right")
if check("the door is not unlocked"):
    robot.turn("dial left")
if check("the door is now unlocked"):
    robot.release("gripper")