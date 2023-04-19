

if check("the robot's gripper is not above the box lid"):
    robot.place("gripper above box lid")
if check("the robot's gripper is above lid and the robot's gripper is not around lid"):
    robot.drop("gripper around box lid")
if check("the robot's gripper is around lid and the robot's gripper is open"):
    robot.close("gripper around box lid")
if check("the robot's gripper is around lid and the gripper is closed"):
    robot.place("box lid on box")