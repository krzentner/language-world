
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle and the robot's gripper is vertically aligned with door handle"):
        robot.pull("door open")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# peg-insert-side-v2: grab the peg and insert it into the hole from the side
def peg_insert_side_v2(robot):
    if check("peg is not vertically aligned with the robot's gripper and the peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole and the peg is not in front of hole"):
        robot.insert("peg into hole")

# block-stack: place the block on top of the other block
def block_stack(robot):
    if check("the robot's gripper is not vertically aligned with the block and the robot's gripper is not above the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is not around the block"):
        robot.close("the gripper around the block")
    if check("the robot's gripper is closed and the robot's gripper is above the block"):
        robot.lift("the block up")
    if check("the robot's gripper is vertically aligned with the goal and the robot's gripper is above the goal"):
        robot.place("the block on the goal")

# button-press: push the button down
def button_