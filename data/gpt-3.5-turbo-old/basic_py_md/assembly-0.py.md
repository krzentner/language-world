# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is not near the wrench"):
        robot.move("gripper to wrench")
    if check("the robot's gripper is near the wrench and the wrench is not inside the gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move("gripper to peg")
    if check("the robot's gripper is above the peg and the gripper is open"):
        robot.drop("the wrench around the peg")