
    # Steps:
    #  1. Put gripper below puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # Since we're pushing the puck backwards, we need to move the gripper below
    # the puck to get traction.
    # We'll have to move the gripper over the puck from the top.
    if check("the robot's gripper is not above puck and the robot's gripper is not near puck"):
        robot.move("gripper below puck")
    # If the gripper is above the puck and not near it, we should move the
    # gripper down to the puck to slide it.
    if check("the robot's gripper is above puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")