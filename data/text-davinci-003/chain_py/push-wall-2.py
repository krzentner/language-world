
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck around wall to goal
    # To push the puck around the wall, we'll need to make sure that the gripper
    # is vertically aligned with the puck.
    # Put gripper above puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # Push gripper into top of puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # Slide the puck around the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.align("the wall")
        robot.slide("the puck to the goal")