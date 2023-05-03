

# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper into back of puck
    #  3. Slide puck to goal
    # To push the puck backwards, move the gripper behind the puck and push down
    # on it from behind.
    # First, put the gripper behind the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not behind the puck"):
        robot.move_gripper("behind the puck")
    # If the gripper isn't near the puck, put it near the puck.
    if check("the robot's gripper is not near puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is behind puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")