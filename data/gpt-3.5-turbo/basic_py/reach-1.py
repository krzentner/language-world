if check("the robot's arm is not extended towards the target location"):
        robot.extend("the arm towards the target location")
    if check("the robot's gripper is not vertically aligned with the target location"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is not open"):
        robot.open("the gripper")
    if check("the robot's gripper is open and the robot's gripper is above the target location"):
        robot.grab("the object at the target location")