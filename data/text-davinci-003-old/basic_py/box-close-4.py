
    if check("the robot's gripper is not above lid"):
        robot.place("gripper above lid")
    if check("lid is not right of the robot's gripper and lid is not forward aligned with the robot's gripper"):
        robot.grab("lid")
    if check("the robot's gripper is above the box and robot's gripper is forward aligned with box"):
        robot.place("lid onto box")
    if check("lid is on box"):
        robot.release("lid")