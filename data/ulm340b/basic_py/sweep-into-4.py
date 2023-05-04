
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the robot's gripper is not near the goal"):
        robot.put("cube at goal")

# push-into: push the cube to the target location
def push_into(robot):
    if check("the robot's gripper is not vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near the cube"):
        robot.put("gripper into cube")
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.push("the cube to the goal")

# turn-and-place: hold a puck and place it into the container
def turn_and_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around the puck"):
        robot.put("gripper around puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around the puck and the robot's gripper is not near the container"):
        robot.grab("container")
    if check("the robot's gripper is near the container and the puck is below the robot's gripper"):
        robot.put("puck into container")

# turn-and-reach: hold a puck and place it at the target location
def turn_and_reach(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around the puck"):
       