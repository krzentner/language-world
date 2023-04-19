# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):

# Steps:
# 1. Put gripper above the puck
# 2. Push gripper into top of puck
# 3. Move gripper to the wall's location
# 4. Move gripper to the other side of the wall
# 5. Slide puck to goal

# The robot can use a similar strategy to push the puck to the target
# location as in the `push` function. However, with the wall in the way,
# we need to move the gripper to both sides of the wall.

# If the gripper is not above the puck, move it there
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")

# If the gripper isn't around the puck, put it around the puck.
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)

# If the gripper is near the puck, we've probably trapped the puck and can
# move it to the wall's location.
if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
    robot.move_gripper("above the wall")

# If the gripper is above the wall, move it to the other side of the wall.
if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with the ground"):
    robot.move_gripper("vertically aligned with the ground")

# Once on the other side of the wall, we can slide the puck to the target location
if check("the robot's gripper is above puck"):
    robot.move_gripper("above the target location")