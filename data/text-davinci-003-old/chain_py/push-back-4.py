
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper downwards to hold the puck
    #  3. Slide the puck backwards to the target location
    # First, place the gripper above the puck.
    if check("the robot's gripper is not above puck"):
        robot.put("the gripper above the puck")
    # If the gripper is not near the puck, move it closer.
    if check("the robot's gripper is not near puck and the robot's gripper is open"):
        robot.push("the gripper into the puck")
    # Once the gripper is near the puck, we can trap it by pushing the gripper
    # downwards.
    # We need to close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.close("gripper around puck")
    # Now that the puck is trapped in the gripper, arrow slide it backwards to the
    # target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the puck is not at goal"):
        robot.slide("the puck backward to the goal")