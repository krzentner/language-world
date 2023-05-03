# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Check for wall
    #  4. If wall present, back up gripper
    #  5. Move left or right
    #  6. Move gripper forward
    #  7. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper. If a wall is present, it must move around it
    # first.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # Check for wall
        if check("there is a wall in front of the robot's gripper"):
            robot.move_gripper("behind the puck")
            # move left or right
            if check("the robot's gripper is aligned with the wall"):
                robot.move_gripper("right of the wall")
            # move forward
            if check("the robot's gripper is behind the wall"):
                robot.move_gripper("near the puck")
        robot.move_gripper("above the target location")