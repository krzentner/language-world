

If check("the robot's gripper is not above the box lid"):
    robot.place("gripper above box lid")
if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
    robot.drop("gripper around box lid")
if check("the robot's gripper is around the box lid and the robot's gripper is open"):
    robot.close("gripper around box lid")
if check("the robot's gripper is above the box lid and the lid is not near the box"):
    robot.move("gripper near the box")
if check("the robot's gripper is near the box and the lid is below the robot's gripper"):
    robot.place("box lid onto box")