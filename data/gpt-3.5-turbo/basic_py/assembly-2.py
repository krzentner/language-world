if check("the robot's gripper is not near the wrench and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.grab("the wrench")
    if check("the robot's gripper is not near the peg and the robot's gripper is not around the peg"):
        robot.move("gripper to above the peg")
    if check("the robot's gripper is above the peg and the robot's gripper is not around the peg"):
        robot.drop("gripper around the peg")
    if check("the robot's gripper is around the peg and the wrench is still in the gripper"):
        robot.rotate("the wrench around the peg until tight")