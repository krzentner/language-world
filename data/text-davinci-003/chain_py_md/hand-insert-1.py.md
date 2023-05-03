

The task is as follows:

# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, we need to put the gripper above the puck.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # As long as the gripper is above the puck, lower it around the puck.
    if check("the robot's gripper is above puck and the robot's grip is not around puck"):
        robot.drop("gripper about puck")
    # Now that the gripper is around the puck, close the gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If the gripper is closed around the puck, move it to the goal.
    if check("the robot's gripper is closed around the puck"):
        robot.move("puck to goal")