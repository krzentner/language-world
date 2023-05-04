
    if check("the robot's gripper is not above the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("handle up")

# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not above the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not near the handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.push("handle down")

# lever-pull: pull up the lever
def lever_pull(robot):
    if check("the robot's gripper is not around the lever handle"):
        robot.put("gripper around lever handle")
    if check("the robot's gripper is around the lever handle and the lever is upright"):
        robot.pull("lever up")

# lever-push: push down the lever
def lever_push(robot):
    if check("the robot's gripper is not around the lever handle"):
        robot.put("gripper around lever handle")
    if check("the robot's gripper is around the lever handle and the lever is not down"):
        robot.push("lever down")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# pick-place-bin: pick up the puck and hold it at the target location
def pick_place_bin(robot):
    if check("the robot'