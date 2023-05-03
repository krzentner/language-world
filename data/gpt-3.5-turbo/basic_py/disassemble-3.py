if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is not above the peg"):
        robot.move("gripper to above peg")
    if check("the robot's gripper is above the peg and the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench"):
        robot.pull("wrench off peg")