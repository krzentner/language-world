# Steps:
#  1. Put gripper near the edge of the door
#  2. Push the door closed
# If the gripper is not near the edge of the door, move it there.
if check("the robot's gripper is not near the edge of the door"):
    robot.put("gripper near the edge of the door")
# If the gripper is near the edge of the door, push the door closed.
if check("the robot's gripper is near the edge of the door"):
    robot.push("door closed to the target location")