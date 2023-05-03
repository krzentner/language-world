
    if check("the robot's gripper is not near the peg"):
        robot.grab("below peg")
    if check("the robot's gripper is near the peg"):
        robot.push("peg in hole")
    if check("peg halfway in hole"):
        robot.push("peg in hole harder")

# lever-left: pull the lever from left to right
def lever_left(robot):
    if check("the robot's gripper is not horizontally aligned with the lever"):
        robot.put("gripper next to lever")
    if check("the robot's gripper is horizontally aligned with the lever"):
        robot.push("lever left to right")