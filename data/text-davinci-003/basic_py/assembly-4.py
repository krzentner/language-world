
    if check("the robot's gripper is not forward aligned with the wrench and the robot's gripper is not horizontally aligned with wrench"):
        robot.put("gripper forward of wrench")
    if check("the robot's gripper is horizontally aligned with wrench and the robot's gripper is not near wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is forward aligned with wrench and the robot's gripper is near wrench"):
        robot.align("wrench around peg")