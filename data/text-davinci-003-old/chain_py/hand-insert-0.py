
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move gripper to goal
    # We need to put the gripper above the puck before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    # Once the gripper is lined up above the puck, we should be able to grab the
    # puck by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    # Once the gripper is around the puck, we can just close the gripper.
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move("gripper to goal")