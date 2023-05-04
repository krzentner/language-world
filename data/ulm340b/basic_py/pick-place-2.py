
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is not above puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.grab("the puck")
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.move("the puck to the goal")

# stack: place the green puck on top of the red puck
def stack(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.grab("the puck")
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.put("the puck above the other puck")

# unstack: lift the green puck from the red puck
def unstack(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.grab("the puck")
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.move("the puck above the other puck")

# turn-lever-ccw: pull the lever down to turn it counter-clockwise
def turn_lever_ccw(robot):
    if check("the robot's gripper is not vertically aligned with the lever handle"):
        robot.put("gripper above lever handle")
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around lever handle"):
        robot.put("gripper around lever handle")
    if check("the robot's gripper is around the lever handle and the lever handle is above the robot's gripper"):
        robot.push("down on lever handle")

# turn-lever-cw: push the lever up to turn it clockwise
def turn_lever_cw(robot):
    if check("the robot's gripper is not