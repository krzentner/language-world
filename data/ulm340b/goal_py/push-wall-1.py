
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper on puck
    #  3. Close gripper on top of puck
    #  4. Push the gripper into the puck
    #  5. Slide the puck to the goal
    # If the gripper isn't above the puck, move it above the puck so that we
    # don't hit it while dropping it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Because there's a small wall, we have to start the push by putting the
    # gripper down on the puck, unlike "push".
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Now that the gripper is down and the puck is below it, if the gripper is
    # open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.move_gripper("above the target location")

# push-left: slide the puck to the left of the small obstacle
def push_left(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper on puck
    #  3. Close gripper on top of puck
    #  4. Push the gripper into the puck
    #  5. Slide the puck around the obstacle
    # If the gripper isn't above the puck, move it above the puck so that we
    # don't hit it while dropping it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Because there's a small obstacle, we have to start the push by putting the
    # gripper down on the puck, unlike "push".
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("near the