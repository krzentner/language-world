# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):

# Steps:
#   1. Move the gripper to the puck while avoiding the wall
#   2. Grab the puck
#   3. Lift the puck over the wall
#   4. Move the puck to the target location
#   5. Hold the puck steady

# First check if there is wall in the way of the gripper and puck
if check("there is a wall between the gripper and the puck"):
    # Move the gripper just above the wall
    robot.move_gripper("above the wall")

# Move the gripper close to the puck while avoiding the wall
if check("the gripper is not near the puck and the gripper is not blocked by the wall"):
    robot.move_gripper("near the puck", safe_path=True)

# Grab the puck
if check("the gripper is near the puck"):
    robot.move_gripper("around the puck", close_gripper=True)

# Lift the puck over the wall
if check("the gripper is holding the puck"):
    robot.move_gripper("above the wall", safe_path=True)

# Move the puck to the target location
if check("the gripper is above the target location"):
    robot.move_gripper("near the target location")

# Hold the puck steady
if check("the gripper is above the target location"):
    robot.hold_gripper()