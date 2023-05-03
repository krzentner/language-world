if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above the box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around the box lid")
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around the box lid")
    if check("the robot's gripper is vertically aligned with the box and the robot's gripper is closed"):
        robot.put("box lid on top of box")