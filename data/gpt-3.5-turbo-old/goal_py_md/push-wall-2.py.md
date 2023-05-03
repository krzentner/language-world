# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Lift gripper over wall
    #  3. Push gripper into top of puck
    #  4. Slide puck to goal
    # If the wall is not in between the puck and the target location, perform the push function
    if check("the wall is not between the puck and the target location"):
        push(robot)
    else:
        # Move the gripper over the wall
        if check("the robot's gripper is not above the wall"):
            robot.move_gripper("above the wall")
        # Move the gripper down to the puck
        if check("the robot's gripper is above the wall and the robot's gripper is not near puck"):
            robot.move_gripper("above the puck", close_gripper=True)
        # If the gripper is near the puck, we've probably trapped the puck and can
        # slide it past the wall to the target location.
        # Close the gripper to make sure we keep control of the puck.
        if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
            robot.move_gripper("above the target location")