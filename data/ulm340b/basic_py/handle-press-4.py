
    if check("the robot's gripper is not around handle and handle is left of the robot's gripper"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.push("handle down")

# button-press-side: push the button to the right
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button to the right")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# handle-press-side: push the handle to the right
def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("handle to the right")

# pick-place-side: pick up the puck and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal