if check("the robot's gripper is not vertically aligned with the wrench and the wrench is on the peg"):
        robot.move("gripper above wrench and peg")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is on the peg"):
        robot.grab("wrench")
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is holding the wrench and the peg and the peg is horizontally aligned with the hole and the wrench is in front of the peg"):
        robot.pull("wrench off peg")