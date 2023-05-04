
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is not near the door handle and the door handle is left of the robot's gripper"):
        robot.push("gripper against door")
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.push("door closed")

# turn-crank: turn the crank
def turn_crank(robot):
    if check("the robot's gripper is not horizontally aligned with the crank and the crank is not left of the robot's gripper"):
        robot.grab("crank")
    if check("the robot's gripper is forward aligned with the crank"):
        robot.turn("crank clockwise")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the puck is not above the robot's gripper"):
        robot.put("puck above the robot's gripper")
    if check("the puck is not in the robot's gripper"):
        robot.grab("puck")
    if check("the puck is in the robot's gripper"):
        robot.place("puck at goal")

# pick-out-of-hole: pick the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the peg is not above the robot's gripper"):
        robot.put("gripper above the peg")
    if check("the peg is not in the robot's gripper"):
        robot.grab("peg")
    if check("the peg is in the robot's gripper"):
        robot.hold("peg at goal")

# remove-microwave: open the microwave, remove the plate and hold it at the target location
def remove_microwave(robot):
    if check("the robot's gripper is not near the microwave