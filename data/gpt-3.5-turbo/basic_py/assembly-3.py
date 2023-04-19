if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is above the wrench"):
        robot.move("gripper to the right of the wrench")
    if check("the robot's gripper is near the wrench"):
        robot.grab("the wrench")
    if check("the robot's gripper is vertically aligned with the peg and the peg is not between the jaws of the wrench"):
        robot.move("gripper to the left of the peg")
    if check("the peg is between the jaws of the wrench"):
        robot.rotate("the wrench to tighten the peg")