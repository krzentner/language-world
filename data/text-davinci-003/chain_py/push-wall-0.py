
    # Steps:
    #  1. Put gripper against wall above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # We need the gripper to be placed relatively high up so it can still go
    # beyond the wall in order to push the puck.
    if check("the robot's gripper is not against wall above puck"):
        robot.put("gripper against wall above puck")
    # After the gripper is placed above the puck, we can move the gripper
    # downward, making sure that it's the gripper that goes over the wall, not the
    # puck.
    if check("the robot's gripper is against wall above puck and the robot's gripper is not near puck"):
        robot.push("gripper into top of puck")
    # Finally, when the gripper is close enough to the puck, we can slide the
    # puck to the goal.
    if check("the robot's gripper is near the puck"):
        robot.slide("to goal")