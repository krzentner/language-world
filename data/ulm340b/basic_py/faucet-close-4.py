
    if check("the robot's gripper is not near the faucet handle"):
        robot.grab("the faucet handle")
    if check("the robot's gripper is near the faucet handle and the faucet handle is left of the robot's gripper"):
        robot.close("the faucet")

# microwave-close: close the door of the microwave
def microwave_close(robot):
    if check("the robot's gripper is not vertically aligned with the microwave handle and the robot's gripper is below the microwave handle"):
        robot.move("gripper to right of microwave handle")
    if check("the robot's gripper is near the microwave handle"):
        robot.slide("door closed")
    if check("the robot's gripper is in front of the microwave handle"):
        robot.push("door closed harder")

# plug-socket-pull: unplug the plug from the socket
def plug_socket_pull(robot):
    if check("the robot's gripper is not near the plug"):
        robot.grab("the plug")
    if check("the robot's gripper is around the plug"):
        robot.pull("the plug from the socket")

# dishwasher-open: pull the door of the dishwasher open
def dishwasher_open(robot):
    if check("the robot's gripper is not vertically aligned with the dishwasher handle and the robot's gripper is below the dishwasher handle"):
        robot.move("gripper to right of dishwasher handle")
    if check("the robot's gripper is near the dishwasher handle"):
        robot.slide("door left")
    if check("the robot's gripper is in front of the dishwasher handle"):
        robot.push("door left harder")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is not around the door handle"):
        robot.grab("the door handle")
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.push("the door closed")

# button-press-side: push the button to the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is near button and the robot's gripper is open"):
        robot.close("gripper on button")
 