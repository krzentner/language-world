
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck in goal")

# hand-insert-disc: pick up the puck and move it to the target location
def hand_insert_disc(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck in goal")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not above lever and the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is above lever and the robot's gripper is not near lever"):
        robot.move("gripper to the lever")
    if check("the robot's gripper is above lever and the robot's gripper is near lever"):
        robot.close("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever down")

# bottle-insert: insert the bottle into the hole
def bottle_insert(robot):
    if check("the robot's gripper is not above bottle and the robot's gripper is not vertically aligned with bottle"):
        robot.put("gripper above bottle")
    if check("the robot's gripper is vertically aligned with bottle and the robot's gripper is not near bottle"):
        robot.put("gripper around bottle")
  