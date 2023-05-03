# door-lock: turn the dial on the door
# def door_lock(robot):

# Steps:
# 1. Put gripper above the dial
# 2. Drop gripper around the dial
# 3. Turn the dial to the right to lock the door
# 4. Pull the gripper up and drop it to release the dial

# First, put the gripper above the dial
if check("the robot's gripper is not above the dial"):
    robot.place("gripper above the dial")

# Next, drop the gripper around the dial
if check("the robot's gripper is not around the dial" and "the robot's gripper is open"):
    robot.drop("gripper around the dial")

# Now that the gripper is around the dial, turn it to the right to lock the door
if check("the robot's gripper is around the dial"):
    robot.turn("the dial to the right")

# Lastly, pull the gripper up and drop it to release the dial
if check("the robot's gripper is around the dial and the dial is turned to the right"):
    robot.pull("the gripper up")
    robot.drop("gripper to release the dial")