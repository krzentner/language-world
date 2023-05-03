# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        if check("the puck is not above the target location"):
            robot.move("puck to goal")
        if check("the puck is above the target location"):
            robot.release("the puck")