# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.place("box lid on the box")