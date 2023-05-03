
    if check("the robot's gripper is not over the lid"):
        robot.put("gripper over the lid")
    if check(" the robot's gripper is around the lid and the robot's gripper is open"):
        robot.close("gripper around the lid")
    if check("the robot's gripper is over the lid and the robot's gripper is closed"):
        robot.place("lid on box")