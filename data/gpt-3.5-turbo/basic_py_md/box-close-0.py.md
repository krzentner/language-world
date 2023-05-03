# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is open and not around box lid"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is around box lid"):
        robot.lift("box lid")
    if check("the box lid is lifted and the robot's gripper is near the box and the robot's gripper is forward aligned with the box lid"):
        robot.put("box lid on box")
    if check("the box lid is on the box and the robot's gripper is not around the box"):
        robot.drop("gripper around box")