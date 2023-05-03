# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Slide puck to target location
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is above the puck, put it around the puck.
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is around the puck, we can start sliding it towards the
    # target location.
    if check("the robot's gripper is near the puck and the puck is not at the target location"):
        robot.move_gripper("near the target location")