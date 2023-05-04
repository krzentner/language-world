
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("cube to goal")

# wipe: grab the cube and move it sideways to the target location
def wipe(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("cube to goal")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# reach-camera-v1: reach to the target location
def reach_camera_v1(robot):
    if check("the robot's gripper is not above target"):
        robot.place("the gripper above target")
    if check("the robot's gripper is near target"):
        robot.drop("the gripper at target")
    if check("the robot's gripper is on target"):
