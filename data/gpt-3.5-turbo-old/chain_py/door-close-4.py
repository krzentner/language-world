# Steps:
#  1. Put gripper roughly near the door
#  2. Push the door closed
# If the gripper is not near the door, move it to be nearby.
if check("the robot's gripper is not near the door"):
    robot.move("gripper near the door")
# If the door is aligned with the gripper, we can push it closed.
if check("the robot's gripper is vertically aligned with door"):
    robot.push("door closed")