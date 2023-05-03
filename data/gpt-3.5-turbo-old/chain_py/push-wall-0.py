# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck towards wall
    #  4. Move gripper to the other side of the wall
    #  5. Slide puck towards goal
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
    # slide it to the left towards the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck towards the wall")
    # Move the gripper to the right side of the wall to continue sliding the
    # puck towards the goal.
    if check("the puck is against the wall"):
        robot.move("the gripper to the other side of the wall")
    # Slide the puck towards the goal.
    if check("the robot's gripper is near the puck and the puck is on the other side of the wall"):
        robot.slide("the puck towards the goal")