# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the wrench is not between the robot's gripper and the peg and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the wrench is not between the robot's gripper and the peg and the robot's gripper is closed"):
        robot.open("gripper")
    if check("the wrench is not near the peg and the robot's gripper is open"):
        robot.put("gripper near peg and wrench")
    if check("the wrench is between the robot's gripper and the peg and the robot's gripper is open"):
        robot.close("gripper around wrench and peg")