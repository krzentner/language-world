
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
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
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")

# push-side: slide the puck sideways to the target location
def push_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper sideways into side of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't right of the gripper as seen from above, move the
    # gripper above the puck.
    # Because we're moving the puck sideways, we want to push it on the side,
    # not in the center.
    if check("the robot's gripper is not above puck and the robot's gripper is not horizontally aligned with the puck"):
        robot.move_gripper("horizontally aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    #