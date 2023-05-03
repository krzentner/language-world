# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("wrench is not within range of the gripper"):
        robot.move("gripper to the wrench")
    if check("the gripper is not around the wrench"):
        robot.grab("the wrench")
    if check("the gripper is not vertically aligned with the peg and the wrench is held open"):
        robot.release("the wrench")
        robot.move("gripper to the peg")
        robot.grab("the peg")
        robot.move("gripper to the wrench")
        robot.grab("the wrench")
    if check("the gripper is vertically aligned with the peg and the wrench is held open"):
        robot.release("the wrench")
        robot.move("gripper around the peg and the wrench")
        robot.close("the gripper around the peg and the wrench")