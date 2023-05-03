
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide the puck to goal
    #  4. Move the puck past the wall
    # Just like the push task, we first need to put the gripper above the puck
    # and push the gripper down into the top of the puck to trap it.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # As long as the wall is still blocking the way, let's continue sliding the
    # puck towards the goal.
    if check("the puck is blocked by the wall and the puck is below the robot's gripper"):
        robot.slide("the puck to the wall")
    # If the puck is next to the wall, try to move it along the wall until it's
    # past the wall.
    if check("the puck is next to wall"):
        robot.move("the puck along wall")
    # Once the puck is past the wall, slide it to the goal.
    if check("the puck is beyond the wall"):
        robot.slide("puck to goal")