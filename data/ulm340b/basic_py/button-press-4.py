
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper at the button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button down")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# door-close: pull the door closed
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")

# grasp: grasp the object
def grasp(robot):
    if check("the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is open and the object is not left of the robot's gripper and the object is not forward aligned with the robot's gripper"):
        robot.grab("object")
    if check("the object is in the robot's gripper"):
        robot.grasp("object")

# grasp-left: grasp the object with the left gripper
def grasp_left(robot):
    if check("the robot's left gripper is not forward aligned with the object"):
        robot.move("left gripper to the object")
    if check("the robot's left gripper is forward aligned with the object and the object is not left of the robot's left gripper"):
        robot.grab("object with left gripper")
    if check("the object is left