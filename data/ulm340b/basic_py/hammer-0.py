
    if check("hammer is not aligned with nail"):
        robot.align("hammer with nail")
    if check("hammer is aligned with nail"):
        robot.hit("nail with hammer")

# slide-drawer-close: slide the drawer closed from above
def slide_drawer_close(robot):
    if check("the robot's gripper is not above drawer"):
        robot.put("gripper above drawer")
    if check("the robot's gripper is above the drawer"):
        robot.push("drawer left")

# slide-drawer-open: slide the drawer open from above
def slide_drawer_open(robot):
    if check("the robot's gripper is not above drawer"):
        robot.put("gripper above drawer")
    if check("the robot's gripper is above drawer"):
        robot.push("drawer right")

# stack: place the puck on the box
def stack(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is forward aligned with the puck"):
        robot.pick("puck")
    if check("the robot's gripper is not above the box"):
        robot.put("gripper above the box")
    if check("the robot's gripper is above the box"):
        robot.put("the puck on the box")

# stir: stir the contents of the pot using the spoon
def stir(robot):
    if check("the robot's gripper is not above the pot"):
        robot.place("the robot's gripper above the pot")
    if check("the robot's gripper is above the pot"):
        robot.put("the spoon into the pot")
    if check("the robot's gripper is inside the pot"):
        robot.stir("the spoon")

# turn-switch: flip the switch to the on position
def turn_switch(robot):
    if check("the robot's gripper is not vertically aligned with the switch"):
        robot.place("gripper above switch")
    if check("the robot's gripper is vertically aligned with the switch and the switch is not forward aligned with the robot's gripper"):
        robot.grab("switch")
   