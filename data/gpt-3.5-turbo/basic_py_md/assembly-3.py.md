# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is above the wrench and the robot's gripper is not around wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around wrench"):
        robot.rotate_clockwise("wrench onto peg")
    if check("the wrench is firmly wrapped around the peg"):
        robot.done()