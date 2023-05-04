
    if check("the robot's gripper is not near sweep cube"):
        robot.push("gripper to sweep cube")
    if check("the robot's gripper is forward aligned with the sweep cube"):
        robot.put("sweep cube on robot's gripper")
    if check("the sweep cube is on the robot's gripper and the robot's gripper is not at the goal"):
        robot.put("sweep cube at goal")

# sweep-onto: grab the cube and place it on top of the target cube
def sweep_onto(robot):
    if check("the robot's gripper is not above the sweep cube"):
        robot.put("gripper above sweep cube")
    if check("the robot's gripper is above the sweep cube and the robot's gripper is not around the sweep cube"):
        robot.put("gripper around sweep cube")
    if check("the robot's gripper is around the sweep cube and the robot's gripper is open"):
        robot.put("robot's gripper closed")
    if check("the robot's gripper is around the sweep cube and the robot's gripper is closed"):
        robot.put("sweep cube above target cube")
    if check("the robot's gripper is above the target cube and the robot's gripper is closed"):
        robot.put("sweep cube on target cube")

# pick-place-into: pick up the puck and place it in the container
def pick_place_into(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not around puck"):
        robot.put("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.put("robot's gripper closed")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.put("puck above container")
    if check("the robot's gripper is above the container and the robot's gripper is closed"):
        robot.put("puck inside container")

# push-pick-place: push the puck to the target and pick up and hold the puck
def push_pick_place(robot):
    if check("the robot'