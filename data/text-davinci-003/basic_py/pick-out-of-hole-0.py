
    if check("the robot's gripper is not vertically aligned and below peg"): 
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is above the peg"):
        robot.place("peg at goal")