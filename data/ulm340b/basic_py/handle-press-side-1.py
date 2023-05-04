
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.put("gripper in front of handle")
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is above the handle"):
        robot.push("gripper down on handle")

# handle-press-topdown: push down the handle from above
def handle_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("gripper down on handle")

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.put("gripper in front of handle")
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is below the handle"):
        robot.pull("gripper up on handle")

# handle-pull-topdown: pull up the handle from above
def handle_pull_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("gripper up on handle")

# block-pickup-side: pick up the block from the side
def block_pickup_side(robot):
    if check("the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not forward aligned with block and the robot's gripper is open"):
        robot.put("gripper in front of block")
    if check("the robot's gripper is forward aligned with block and the robot's gripper is open"):
        robot.grab("block")

# block-pickup-topdown: pick up the block from above
def block_pickup_topdown(robot):
    if check("the robot's gripper is not above block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is open"):
        robot.drop("gripper