if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle" and "the drawer is closed"):
        robot.pull("drawer open")

# button-press-sides: push the button from the side
def button_press_sides(robot):
    if check("the robot's gripper is not left of the button and the robot's gripper is not almost vertically aligned with the button"):
        robot.move("gripper to left of button")
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.push("the button")

# pick-up: pick up the object from the target location
def pick_up(robot):
    if check("the robot's gripper is not above pick-up location"):
        robot.reach("to pick-up location")
    if check("the robot's gripper is above pick-up location and the gripper is open"):
        robot.grab("object")
    if check("the robot's gripper is holding object"):
        robot.pull("gripper up")

# door-close: push the door shut
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper around door handle" and "door is open")
    if check("the robot's gripper is almost vertically aligned with the door handle"):
        robot.push("door shut")

# place: release the object at the target location
def place(robot):
    if check("the gripper is not above the target location" and "the gripper is holding an object"):
        robot.reach("to target location")
    if check("the gripper is above the target location" and "the gripper is holding an object"):
        robot.drop("object at target location")

# pick-place-reverse: pick up the object from the target location and hold it backwards
def pick_place_reverse(robot):
    if check("the gripper is not aligned with the pick-up location"):
        robot.reach("to pick-up location")
    if check("the gripper is vertically aligned with object and the gripper is open facing backwards"):
        robot.grab("the object")
    if check("the gripper is holding object facing backwards and the gripper is vertically aligned with the target location"):
        robot.place("the object at target location facing backwards")