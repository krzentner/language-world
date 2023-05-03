
    if check("the robot's gripper is not above lid"):
        robot.place("gripper above lid")
    if check("the robot's gripper is not under lid and the robot's gripper is not around lid"):
        robot.grab("lid")
    if check("the robot's gripper is around lid and the robot's gripper is not above box"):
        robot.lift("lid above box")
    if check("the robot's gripper is above the box"):
        robot.place("lid onto box")