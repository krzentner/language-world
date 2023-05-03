
    if check("the robot's gripper is not vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.grab("cube")
    if check("the robot's gripper is around the cube and the cube is not horizontal aligned with the goal"):
        robot.readjust("cube to the goal")
    if check(" the cube is horizontal aligned with the goal"):
        robot.sweep("cube to the goal")