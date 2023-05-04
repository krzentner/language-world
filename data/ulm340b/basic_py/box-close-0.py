
    if check("the robot's gripper is not above box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not left of box lid and the robot's gripper is not forward aligned with box lid"):
        robot.grab("box lid")
    if check("the robot's gripper is forward aligned with box lid"):
        robot.push("box lid into place")

# pick: grasp the puck
def pick(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# place: place the puck at the target location
def place(robot):
    if check("the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# box-open: pick up the box lid and move it away from the box
def box_open(robot):
    if check("the robot's gripper is not above box lid"):
        robot.place("gripper above box lid")
    if check("the robot's gripper is not forward aligned with box lid"):
        robot.grab("box lid")
    if check("the robot's gripper is forward aligned with box lid"):
        robot.push("box lid up")

# drawer-close-side: pull the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not above the drawer handle and the robot's gripper is not vertically aligned with the drawer handle"):
        robot.place("gripper above drawer handle")
    if check("the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer handle left")

# pick-place-wall: grasp the puck and place it on the wall
def pick_place_wall(robot):
