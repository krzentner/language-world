
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put( "gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.grab("cube")
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.sweep("cube sideways to goal")