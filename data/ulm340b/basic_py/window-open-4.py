
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# pull-drawer-open: pull the drawer open
def pull_drawer_open(robot):
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle and the robot's gripper is open"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# pull-door-open: pull the door open
def pull_door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with door handle and the robot's gripper is open"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.pull("door open")

# pick-place-with-safety-margin: pick up the puck and hold it at the target location
def pick_place_with_safety_margin(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# grasp-bottle-neck-from-top: grasp the neck of the bottle from top
def grasp_bottle_neck_from_top(robot):
    if check("the robot's gripper is not around