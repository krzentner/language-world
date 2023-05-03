
    if check("the robot's gripper is not above the lid"):
        robot.put("gripper above lid")
    if check("the robot's gripper is not near the lid"):
        robot.grab("lid")
    if check("the lid is not below the robot's gripper"):
        robot.lift("lid to bottom of robot's gripper")
    if check("the lid is below the robot's gripper"):
        robot.place("lid on box")