
    if check("the robot's gripper is not near puck"):
        robot.move("the gripper to the puck")
    if check("the robot's gripper is near the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is forward aligned with puck"):
        robot.hold("the puck at the goal")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not below the lever handle"):
        robot.move("the gripper below the lever handle")
    if check("the robot's gripper is below the lever handle"):
        robot.grab("the lever handle")
    if check("the robot's gripper is vertically aligned with lever handle"):
        robot.pull("the lever down")

# lever-push: push the lever up
def lever_push(robot):
    if check("the robot's gripper is not below the lever handle"):
        robot.move("the gripper below the lever handle")
    if check("the robot's gripper is below the lever handle"):
        robot.grab("the lever handle")
    if check("the robot's gripper is vertically aligned with lever handle"):
        robot.push("the lever up")

# knob-turn-right: turn the knob counterclockwise
def knob_turn_right(robot):
    if check("the robot's gripper is not below the knob handle"):
        robot.move("the gripper below the knob handle")
    if check("the robot's gripper is below the knob handle"):
        robot.grab("the knob handle")
    if check("the robot's gripper is vertically aligned with knob handle"):
        robot.rotate("the knob counterclockwise")

# knob-turn-left: turn the knob clockwise
def knob_turn_left(robot):
    if check("the robot's gripper is not below the knob handle"):
        robot.move("the gripper below the knob handle")
    if check("the robot's gripper is below the knob handle"):
        robot.grab("the knob handle")
    if check("the robot's gripper is vertically aligned with knob handle"):
        robot.rotate("the knob clockwise")

# peg-insert-topdown: push the peg into the hole from above
def peg_insert_topdown(robot):
    if check("the robot