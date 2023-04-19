

Steps:
1. Put gripper behind the handle
2. Drop gripper around handle
3. Pull the handle up

# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper behind the handle
    #  2. Drop gripper around handle
    #  3. Pull the handle up
    # First, put the gripper behind the handle, so that the gripper can get a
    # good grip on the handle.
    if check("the robot's gripper is not behind the handle"):
        robot.put("gripper behind handle")
    # As long as the gripper is behind the handle, grab the handle.
    if check("the robot's gripper is behind the handle and the gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is already around the handle and closed, pull the handle up.
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.pull("handle up")