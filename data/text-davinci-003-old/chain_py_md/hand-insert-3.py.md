

The robot can insert the puck by picking it up with its gripper and positioning it at the target location.

# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop the gripper around the puck
    #  3. Close the gripper around the puck
    #  4. Move the puck to the target location
	
    # We need to put the gripper roughly above the puck before we can grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # Once the gripper is around the puck, we can just close the gripper.
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # Now that the gripper is closed around the puck, we can move it to the target location.
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.move("puck to target location")