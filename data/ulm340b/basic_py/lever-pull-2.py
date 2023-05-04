
    if check("the robot's gripper is not near the lever"):
        robot.grab("lever")
    if check("the robot's gripper is aligned with the lever"):
        robot.move("lever up")
    if check("the robot's gripper is not in front of the lever"):
        robot.rotate("lever to vertical")

# door-close: close the door
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around the door handle"):
        robot.push("door close")

# peg-unplug-side: grab the peg and pull it out of the hole
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the peg is forward aligned with the robot's gripper and the peg is not horizontally aligned with the hole"):
        robot.align("peg to hole")
    if check("the peg is horizontally aligned with hole"):
        robot.pull("peg out of hole")

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

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check