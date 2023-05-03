# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not near box lid"):
        robot.grab("box lid")
    if check("the robot's gripper is holding the box lid and the robot's gripper is not above the box"):
        robot.put("gripper above box")
    if check("the robot's gripper is above the box"):
        robot.place("box lid on box")