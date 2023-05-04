
    if check("the robot's gripper is not near the handle"):
        robot.grab("the handle")
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("the gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("the handle down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("the door handle")
    if check("the robot's gripper is forward aligned with the door handle and the robot's gripper is not vertically aligned with the door handle"):
        robot.put("the gripper above the door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("the door closed")

# pick-place-bin: pick up the puck from bin and place it at the target location
def pick_place_bin(robot):
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is below the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is closed"):
        robot.put("puck at goal")

# handle-press: push down the handle from above
def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with handle and the handle is below the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")

# handle-pull: pull the handle up
def handle_pull(robot):
    if check("the robot's gripper is not above handle and handle is below the robot's gripper"):
        robot.put("gripper above handle")
    if check("the robot's gripper is near handle and handle is above the robot's