
    if check("the robot's gripper is not near the puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is near the puck"):
        robot.push("puck to goal")

# slide: slide the puck to the target location
def slide(robot):
    if check("the robot's gripper is not near the puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is near the puck"):
        robot.slide("puck to goal")

# window-open: slide the window open to the left
def block_stack_side(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the block is not left of the robot's gripper and the block is not forward aligned with the robot's gripper"):
        robot.grab("block")
    if check("the robot's gripper is forward aligned with the block and the block is not horizontally aligned with block2"):
        robot.align("block to block2")
    if check("the robot's gripper is horizontally aligned with block2"):
        robot.place("block on block2")

# door-open: pull the door open
def block_stack_on_top(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the block is not left of the robot's gripper and the block is not forward aligned with the robot's gripper"):
        robot.grab("block")
    if check("the robot's gripper is forward aligned with the block and the block is not above block2"):
        robot.lift("block to be above block2")
    if check("the robot's gripper is vertically aligned with block2 and the robot's gripper is open"):
        robot.drop("block on block2")

# drawer-close: push the drawer close
def block_restack(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the block is not left of the robot's gripper and the block is not forward aligned with the robot's gripper"):
        robot.grab("block")
    if check("the