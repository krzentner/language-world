
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.put("the gripper forward of plate")
    if check("the robot's gripper is in front of the plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the plate is right of the robot's gripper"):
        robot.slide("plate back into the goal")

# push-back: push the puck back to the target location
def push_back(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.put("the gripper in front of the puck")
    if check("the robot's gripper is near the puck and the puck is in front of the robot's gripper"):
        robot.push("the puck backward")

# pull-back: pull the puck backwards to the target location
def pull_back(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.put("the gripper behind the puck")
    if check("the robot's gripper is near the puck and the puck is in front of the robot's gripper"):
        robot.pull("the puck backward")

# push-left: push the puck left to the target location
def push_left(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.put("the gripper right of puck")
    if check("the