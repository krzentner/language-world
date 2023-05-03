# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is near wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is around the wrench and the robot's gripper is not above the peg"):
        robot.move("gripper above peg")
    if check("the robot's gripper is above the peg and the wrench is not around the peg"):
        robot.put("wrench around peg")