
    if check("the robot's gripper is not above the lid"):
        robot.place("gripper above lid")
    if check("the robot's gripper is above the lid and the robot's gripper is not around the lid"):
        robot.drop("gripper around lid")
    if check("the robot's gripper is near the lid and the lid is below the robot's gripper"):
        robot.pick("up lid")
    if check("the robot is holding the lid and the lid is not touching the box"):
        robot.place("lid on box")