
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.place("the gripper above the puck")
    if check("the robot's gripper is above the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is above the puck and the robot's gripper is near the puck"):
        robot.slide("the puck to the goal")

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

# pick-place-topdown: pick up the puck and hold it at the target location
def pick_place_topdown(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# push-topdown: slide the puck to the target location
def push_topdown(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the