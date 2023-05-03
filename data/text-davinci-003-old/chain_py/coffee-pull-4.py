
    # Steps:
    #  1. Put gripper around handle of mug
    #  2. Grab handle of mug
    #  3. Pull mug to target location
    # The robot needs to put the gripper around the handle of the mug before it
    # can start to pull the mug.
    if check("the robot's gripper is not around handle of mug"):
        robot.put("gripper around handle of mug")
    # Once the gripper is around the handle, grab it and start to pull.
    if check("the robot's gripper is around handle of mug"):
        robot.grab("handle of mug")
    # The robot can pull the mug to the target location.
    if check("the robot's gripper is around mug handle and  robot's gripper is not near target location"):
        robot.pull("mug to target location")