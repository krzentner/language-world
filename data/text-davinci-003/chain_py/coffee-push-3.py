
    # Steps:
    #  1. Put gripper above handle on mug
    #  2. Grab the handle with the gripper
    #  3. Push the mug to the goal
    #  First, line up the gripper above the handle on the mug.
    if check("the robot's gripper is not above handle on mug"):
        robot.put("gripper above handle on mug")
    # When the gripper is above the handle, grab it by dropping the gripper
    # around it.
    if check("the robot's gripper is above handle on mug and the robot's gripper is not around handle on mug"):
        robot.drop("gripper around handle on mug")
    # Then we can just push the mug to the goal.
    if check("the robot's gripper is around handle on mug"):
        robot.push("mug to goal")