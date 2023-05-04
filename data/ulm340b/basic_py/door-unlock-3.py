
    if check("the robot's gripper is not near the door dial"):
        robot.put("gripper near door dial")
    if check("the robot's gripper is not around the door dial"):
        robot.grasp("door dial")
    if check("the robot's gripper is around door dial"):
        robot.turn("door dial")

# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the door dial"):
        robot.put("gripper near door dial")
    if check("the robot's gripper is not around the door dial"):
        robot.grasp("door dial")
    if check("the robot's gripper is around door dial"):
        robot.turn("door dial")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")

# peg-unplug-side: grab the peg and unplug it from the hole
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not right of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is horizontally aligned with hole"):
        robot.pull("peg out of hole")

# pick-place-with-camera-image: pick up the puck and place it at the target location
def pick_place_with_camera_image(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):