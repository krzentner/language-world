
    if check("the robot's gripper is not near the soccer ball"):
        robot.place("gripper near ball")
    if check("the robot's gripper is near the soccer ball"):
        robot.push("soccer ball to goal")

# pick-place-wall: pick up the puck and hold it at the target location
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# lever-pull: pull the handle of the lever
def lever_pull(robot):
    if check("the robot's gripper is not near lever"):
        robot.place("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not near lever"):
        robot.place("gripper around lever")
    if check("the robot's gripper is near lever"):
        robot.pull("lever")

# peg-insert-back: grab the peg and insert it into the hole from behind
def peg_insert_back(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# push-back: push the puck back into the target location
def push_back(robot):
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("