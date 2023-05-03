if check("the robot's gripper is not above the wrench"):
    robot.place("gripper above wrench")
if check("the robot's gripper is not around the peg"):
    robot.grab("the wrench")
if check("the wrench is not around the peg"):
    robot.rotate("wrench around the peg")
if check("the wrench is around the peg"):
    robot.tighten("wrench to secure the peg")