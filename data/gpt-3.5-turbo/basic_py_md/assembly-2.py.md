# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around wrench and the gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is near wrench and the gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is around wrench and the wrench is not near the peg"):
        robot.reach("the wrench to the peg")
    if check("the wrench is near the peg and the wrench is not around the peg"):
        robot.grab("the wrench and the peg")
    if check("the wrench and the peg are both in the gripper"):
        robot.rotate("the wrench around the peg")
    if check("the wrench is wrapped around the peg"):
        robot.release("the gripper")