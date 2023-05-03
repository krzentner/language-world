# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to wall
    #  4. Lift puck over wall
    #  5. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we can try moving the puck towards the
    # wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the wall")
    # If the gripper is near the wall and the puck is not lifted over it, we need
    # to lift the puck over the wall.
    if check("the robot's gripper is near the wall and the puck is not on the other side of the wall"):
        robot.move_gripper("above the wall")
    # Once the puck is on the other side of the wall, slide it towards the goal.
    if check("the puck is on the other side of the wall"):
        robot.move_gripper("above the target location")