
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not left of the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.pull("down on handle")

# handle-press-topdown: push down the handle from above
def handle_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.pull("up on handle")

# handle-pull-up: pull up the handle from above
def handle_pull_up(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("up on handle")

# door-close: close the door by sliding it to the left
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door left")

# plug-socket-side: pull the plug out from the socket
def plug_socket_side(robot):
    if check("the robot's gripper is not near the plug handle"):
        robot.place("gripper above plug")
    if check("the robot's gripper is near the plug handle"):
        robot.pull("plug out of socket")

# plug