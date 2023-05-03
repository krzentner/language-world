# push: slide the puck to the target location
def push(robot):
    # Steps:
    #   1. Put gripper near the puck
    #   2. Align gripper with puck
    #   3. Push the puck to the target location
    # First, put the gripper near the puck so we don't hit it while we're aligning with it.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # Once the gripper is near the puck, align it with the puck.
    if check("the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")
    # Finally, push the puck to the target location.
    if check("the robot's gripper is around the puck and is not near the target location"):
        robot.move_gripper("near the target location")