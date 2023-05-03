# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is at the target location"):
        robot.drop("puck at target location")