
    if check("the robot's gripper is not near the wrench"):
        robot.reach("for wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is not around the wrench"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is around the wrench"):
        robot.put("wrench around peg")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.reach("door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is not forward aligned with the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is forward aligned with the door handle"):
        robot.push("door closed")

# pick-place-wall: pick up the puck and hold it against the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not above puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is above puck and the puck is below the robot's gripper"):
        robot.hold("puck against wall")

# pick-place-bin: pick up the puck and hold it in the target bin
def pick_place_bin(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not above puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is above puck and the puck is below the robot's gripper"):
        robot.place("puck in bin")

# pick-place-wall-notarget: pick up the puck and hold it against the wall
def pick_place_wall_notarget(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
