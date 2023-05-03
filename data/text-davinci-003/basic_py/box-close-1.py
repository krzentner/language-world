
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    if check("the robot's gripper is open and the robot's gripper is vertically aligned with the box lid"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is closed and the robot's gripper is near the box lid"):
        robot.align("box lid to box")
    if check("box lid is aligned with box"):
        robot.let("box lid down")