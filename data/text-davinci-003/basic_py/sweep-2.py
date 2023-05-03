
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.wipe("cube to goal")