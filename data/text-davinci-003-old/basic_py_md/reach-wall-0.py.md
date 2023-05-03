

if check("the robots gripper is not above the wall"):
    robot.put("gripper above wall")
if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with target"):
    robot.reach("gripper above target")
if check("the robot's gripper is above the wall and the robot's gripper is vertically aligned with target"):
    robot.put("gripper in front of target")
if check("the robot's gripper is not near target"):
    robot.reach("gripper near target")