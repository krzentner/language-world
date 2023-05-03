
    if check("the robot's gripper is not directly above the door lock"):
        robot.put("gripper above door lock")
    if check("the robot's gripper is directly above the door lock and the robot's gripper is open"):
        robot.put("gripper around door lock")
    if check("the robot's gripper is around the door lock and the door is not locked yet"):
        robot.turn("dial to lock")