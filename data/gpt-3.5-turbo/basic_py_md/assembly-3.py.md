# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not vertically aligned with the wrench and the gripper is not open"):
        robot.place("gripper above the wrench")
    if check("the robot's gripper is above the wrench and the gripper is open"):
        robot.close("gripper around the wrench")
    if check("the robot's gripper is holding the wrench and the gripper is above the peg"):
        robot.place("gripper above the peg")
    if check("the wrench is vertically aligned with the peg and the gripper is not around the peg"):
        robot.put("gripper around the peg")
    if check("the wrench is around the peg"):
        robot.release("gripper")