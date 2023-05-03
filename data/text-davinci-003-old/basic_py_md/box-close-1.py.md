

if check("the robot's gripper is not near the box lid"):
        robot.move("gripper above the box lid")
    if check("the robot's gripper is not holding the box lid"):
        robot.drop("gripper around the box lid")
    if check("the robot's gripper is holding the box lid"):
        robot.move("gripper above the box")
    if check("the robot's gripper is above the box and the box lid is not in place"):
        robot.place("box lid onto the box")