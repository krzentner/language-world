
    # Steps:
    #  1. Put gripper behind the puck
    #  2. Push gripper into the back of the puck
    #  3. Slide puck backwards to the goal
    # The robot can slide the puck backwards from its current location by
    # trapping it by pushing down on it from behind and moving the gripper.
    # If the puck isn't behind the gripper, move the gripper behind the puck.
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper behind the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is behind the robot's gripper"):
        robot.slide("the puck backwards to the goal")