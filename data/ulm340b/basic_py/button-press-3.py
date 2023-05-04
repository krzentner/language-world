
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("on button")

# peg-unplug-side: pull the peg out of the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not near the peg and the robot's gripper is not forward aligned with the peg"):
        robot.put("the gripper to the right of the peg")
    if check("the robot's gripper is right of the peg and the peg is not forward aligned with the robot's gripper"):
        robot.grab("the peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with the hole"):
        robot.align("the peg with the hole")
    if check("the peg is vertically aligned with the hole"):
        robot.pull("the peg out of the hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not left of the door handle"):
        robot.move("the gripper to the left of the door handle")
    if check("the robot's gripper is left of the door handle"):
        robot.push("the door closed")

# pick-place-side: grab the puck and place it on the target location from the side
def pick_place_side(robot):
    if check("the robot's gripper is not left of the puck"):
        robot.put("the gripper left of the puck")
    if check("the robot's gripper is left of the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is open"):
        robot.close("the gripper around the puck")
    if check("the robot's gripper is forward aligned with the puck and the robot's gripper is closed"):
        robot.place("the puck on the target")

# pick-place-with-camera: grab the puck and place it at the target location using camera
def pick_place_with_camera(robot):
    if check("the robot's gripper is not left of the puck"):
        robot.put("the gripper left of the puck")