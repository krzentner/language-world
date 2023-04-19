# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the wrench and the robot's gripper is not open"):
        robot.drop("any object in gripper")
        robot.put("gripper above wrench")
    if check("the robot's gripper is open and not around the peg"):
        robot.drop("wrench")
        robot.put("gripper around the peg")