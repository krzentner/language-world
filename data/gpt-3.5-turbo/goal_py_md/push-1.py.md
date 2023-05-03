# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck towards the target
    # First, put the gripper near the puck, so that we can push it without bumping
    # it.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck, push it towards the target.
    if check("the robot's gripper is near the puck and the puck is not near the target location"):
        robot.move_gripper("near the target location")