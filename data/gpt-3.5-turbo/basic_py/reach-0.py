if check("the robot's arm is not extended"):
        robot.extend("arm")
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper above target location")
    if check("the robot's gripper is above the target location"):
        robot.grab("target")
    if check("the target is in the robot's gripper"):
        robot.retract("arm and bring the target to the starting location")