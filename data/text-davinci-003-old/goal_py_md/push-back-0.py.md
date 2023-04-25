

Steps: 
1. Put gripper above puck
2. Push gripper into top of puck
3. Slide puck to goal

We need to put the gripper roughly above puck, so that we don't bump it while trying to grab it.
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")

# If the gripper isn't around the puck, put it around the puck.
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)

# If the gripper is near the puck and open, maybe we can grab it by closing
# the gripper.
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move_gripper("left of the target location", close_gripper=True)

# If the gripper is around the puck, we can just push the puck backwards to the 
# target location.
if check("the robot's gripper is around the puck"):
    robot.move_gripper("left of the target location")