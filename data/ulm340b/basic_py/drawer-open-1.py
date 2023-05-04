
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not near button and button is left of the robot's gripper"):
        robot.move("gripper to button")
    if check("the robot's gripper is near button and the button is left of the robot's gripper"):
        robot.slide("button right")

# pick-place-side: pick up the puck and place it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.put("puck at goal")

# pick-place-bin: pick up the puck and place it inside a bin
def pick_place_bin(robot):
    if check("the robot's gripper is not above puck and puck is not right of the robot's gripper"):
        robot.move("gripper to right of puck")
    if check("the robot's gripper is above puck and puck is right of the robot's gripper"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.put("puck in bin")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not near drawer handle and the drawer handle is right of the robot's gripper"):
