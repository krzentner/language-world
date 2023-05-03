# assembly: put the wrench around the peg
# def assembly(robot):
# The robot should first bring the gripper above the wrench and pick it up.
# Then, it should move the gripper above the peg and align the wrench with the peg.
# Finally, it should close the gripper around the wrench, slide it onto the peg, and release it.

def assembly(robot):
    if check("the robot's gripper is not above wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is above wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    if check("wrench is not aligned with peg"):
        robot.align("wrench to peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.put("the wrench onto the peg")
        robot.release("the wrench")