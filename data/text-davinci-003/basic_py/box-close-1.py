
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is above the box lid and the robot's gripper is not around the box lid"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is above the box lid and the robot's gripper is around the box lid"):
        robot.drop("box lid on box")