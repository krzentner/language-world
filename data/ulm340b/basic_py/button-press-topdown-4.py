
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.grab("button")
    if check("the robot's gripper is above the button"):
        robot.push("button down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.push("door closed")

# plug-socket-side: insert the plug into the socket from the side
def plug_socket_side(robot):
    if check("the robot's gripper is not vertically aligned with the plug and the robot's gripper is not aligned with the socket"):
        robot.move("gripper to plug")
    if check("the robot's gripper is vertically aligned with the plug and the robot's gripper is open"):
        robot.put("gripper around plug")
    if check("the robot's gripper is around plug and the robot's gripper is open"):
        robot.close("gripper around plug")
    if check("the robot's gripper is not aligned with socket and the robot's gripper is forward aligned with plug"):
        robot.move("gripper to socket")
    if check("the robot's gripper is forward aligned with the plug and the robot's gripper is forward aligned with the socket"):
        robot.insert("plug into socket")

# peg-unstack-side: remove the top peg from the stack, from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with top peg"):
        robot.move("gripper to top peg")
    if check("the robot's gripper is vertically aligned with top peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is not around peg"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.pull("away from pegs")
    if check("the robot'