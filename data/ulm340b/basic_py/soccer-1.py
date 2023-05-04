
    if check("the robot's gripper is not above soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is above soccer ball"):
        robot.slide("soccer ball into goal")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.put("puck at goal")

# button-press-topdown-wall: push the button down from above
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# open-microwave: open the microwave
def open_microwave(robot):
    if check("the robot's gripper is not vertically aligned with microwave handle"):
        robot.place("gripper above microwave handle")
    if check("the robot's gripper is vertically aligned with microwave handle and the robot's gripper is not near microwave handle"):
        robot.place("gripper around microwave handle")
    if check("the robot's gripper is near microwave handle"):
        robot.pull("open microwave door")

# drawer-close-wall: push the drawer close
def drawer_close_wall(robot):
    if check("the robot's gripper is not near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# put-in-bin-wall: pick up the puck and place it in the bin
def put_in_bin_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck