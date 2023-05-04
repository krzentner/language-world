
    # Steps:
    #  1. Put the gripper near the puck
    #  2. Push the puck around
    # First, we need to move the robot's gripper near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the robot's gripper is near the puck we can try to push the puck around.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")

# push-back: pull the puck to the target location
def push_back(robot):
    # Steps:
    #  1. Put the gripper behind the puck
    #  2. Pull the puck around
    # First, we need to move the robot's gripper behind the puck.
    if check("the robot's gripper is not near the puck and the robot's gripper is not behind the puck"):
        robot.move_gripper("near the puck")
    # If the robot's gripper is near the puck we can try to pull the puck around.
    if check("the robot's gripper is behind the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")

# slide-back: pull the puck to the target location by the back face
def slide_back(robot):
    # Steps:
    #  1. Put the gripper behind the puck
    #  2. Put the gripper near the puck
    #  3. Push the puck around
    # First, we need to move the robot's gripper behind the puck.
    if check("the robot's gripper is not near the puck and the robot's gripper is not behind the puck"):
        robot.move_gripper("near the puck")
    # If the robot's gripper is near the puck and also behind it, we can try to
    # push the puck around.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("around the puck")

# push-back-side: pull the puck to the target location by the right side face
def push_back_side(robot):
    # Steps:
    #  1. Put