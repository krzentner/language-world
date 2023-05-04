
    if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is not near handle"):
        robot.grab("handle")
    if check("the robot's gripper is near handle"):
        robot.pull("handle up")

# lever-pull-side: pull the lever forward from the side
def lever_pull_side(robot):
    if check("the robot's gripper is not near lever and the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever forward")

# peg-insert-side-v2: grab the peg and insert it into the hole from the side
def peg_insert_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.put("gripper around peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# handle-pull-side-v2: pull up the handle from the side
def handle_pull_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is not near handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is near handle"):
        robot.pull("handle up")

# lever-pull-side-v2: pull the lever forward from the side
def lever_pull_side_v2(robot):
    if check("the robot's gripper is not near lever and the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever forward")

# lever-pull: grab the lever and pull it forward
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper