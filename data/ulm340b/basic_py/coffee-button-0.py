
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.place("gripper on button")
    if check("the robot's gripper is near button and the robot's gripper is open"):
        robot.drop("on button")

# peg-unplug-side: grab the peg and remove it from the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.pull("peg out of hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not forward aligned with the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.push("door closed")

# slide: slide the block to the target location
def slide(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above the block and the robot's gripper is not near block"):
        robot.drop("gripper near block")
    if check("the robot's gripper is near the block"):
        robot.slide("block into place")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not below the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's grip