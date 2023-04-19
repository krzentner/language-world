
    if check("the robot's gripper is not above wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.grab("wrench")
    if check("the robot's gripper is around wrench"):
        robot.pull("wrench away from peg")