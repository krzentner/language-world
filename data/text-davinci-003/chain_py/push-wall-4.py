
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck towards wall
    #  4. Slide puck around wall and to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it towards the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck towards the wall")
    # If the puck is near the wall, rotate the puck to go around the wall.
    if check("the puck is near the wall"):
        robot.rotate("the puck around the wall")
    # If the puck is now by the goal and not by the wall, try to move it to the
    # goal.
    if check("the puck is not between the wall and the goal"):
        robot.place("the puck at the goal")