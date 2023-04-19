# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backwards to goal
    # The robot can slide the puck backwards by trapping it by pushing down on it from
    # above while moving the gripper in the opposite direction.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Once the gripper is near the puck, we can trap the puck and slide it backwards.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("behind the puck")
    # Once the gripper is behind the puck, move the gripper and the puck backwards
    if check("the robot's gripper is behind the puck"):
        robot.move_gripper("behind the target location")