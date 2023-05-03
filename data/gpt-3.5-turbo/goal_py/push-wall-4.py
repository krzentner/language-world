# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Lift puck over wall
    #  4. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # lift it over the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the wall")
    # If the gripper is above the wall and aligned with the target location,
    # slide the puck to the target location.
    if check("the robot's gripper is above the wall and the robot's gripper is forward aligned with the target location"):
        robot.move_gripper("above the target location")