
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the wrench is not left of the robot's gripper and the wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not above the peg"):
        robot.put("wrench above peg")
    if check("the robot's gripper is above peg and the wrench is aligned with the peg"):
        robot.align("wrench to peg")
    if check("the robot's gripper is above peg and the wrench is aligned with the peg"):
        robot.drop("wrench around peg")