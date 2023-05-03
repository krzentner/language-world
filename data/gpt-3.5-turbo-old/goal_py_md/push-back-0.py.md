# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backwards to goal
    # The robot can slide the puck backwards by trapping it by pushing down on it from
    # above and moving the gripper away from the goal.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above the puck and the puck is not below the robot's gripper"):
        robot.move_gripper("above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is above the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck and closed, we've probably trapped the puck and can
    # slide it backwards to the target location.
    # Open the gripper to release the puck once it is at the target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location", close_gripper=False)