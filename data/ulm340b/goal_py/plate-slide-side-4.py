
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")

# slide-side: slide the puck sideways into the target location
def slide_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into puck
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