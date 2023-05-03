# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper and puck to the target location
    #  4. Release the puck at the target
    # First, put the gripper roughly above the puck
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, close it to grab the puck
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If the gripper is holding the puck and it's not at the target location yet, move it to the target
    if check("the robot's gripper is closed around the puck and the puck is not at the target location"):
        robot.move("gripper and puck to goal")
    # If the gripper is at the target location, release the puck
    if check("the robot's gripper is at the goal"):
        robot.release("puck at goal")