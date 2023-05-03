# push-back: slide the puck backwards to the target location
def push_back(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.pull("the gripper away from the puck")
    if check("the robot's gripper is not above the goal and the robot's gripper is not vertically aligned with the goal"):
        robot.put("the gripper above the goal")
    if check("the robot's gripper is vertically aligned with the goal"):
        robot.slide("the puck backwards to the goal")