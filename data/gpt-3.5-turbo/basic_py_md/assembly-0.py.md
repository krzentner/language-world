# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is not vertically aligned with the wrench and the gripper is above the wrench"):
        robot.put("gripper above the wrench")
    if check("the robot's gripper is not around the wrench and the gripper is vertically aligned with the wrench"):
        robot.grab("gripper around the wrench")
    if check("the robot's gripper is around the wrench"):
        robot.slide("the wrench onto the peg")
    if check("the wrench is around the peg"):
        robot.rotate("the wrench roughly 90 degrees")
    if check("the wrench is fully wrapped around the peg"):
        robot.rotate("the wrench an additional 45 degrees")