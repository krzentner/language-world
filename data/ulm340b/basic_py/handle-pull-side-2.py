
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("handle is right of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.pull("up on handle")
    if check("the handle is forward aligned with the robot's gripper"):
        robot.pull("handle up higher")

# handle-pull-up: pull up the handle from the top
def handle_pull_up(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("up on handle")
    if check("the handle is forward aligned with the robot's gripper"):
        robot.pull("handle up higher")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.put("gripper around peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.put("peg over hole")
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.insert("peg into hole")

# peg-unstack-side: grab the top peg and lift it off the stack
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with top peg"):
        robot.put("gripper above top peg")
    if check("top peg is not left of the robot's gripper and top peg is not forward aligned with the robot's gripper"):
        robot.grab("top peg")
    if check("the robot's gripper is forward aligned with the top peg"):
        robot.lift("up top peg")

# peg-unstack-topdown: grab the top peg and lift it off the stack
def peg_unstack