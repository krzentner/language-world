
    # Steps:
    #  1. Put gripper above the plate
    #  2. Put gripper around plate
    #  3. Push plate back into target location
    #  4. Pull gripper out from the plate
    # If the robot's gripper is not above the plate, move it above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Put the robot's gripper around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is not above the plate"):
        robot.move_gripper("around the plate")
    # Slide the plate into the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("near the plate")
    # Once the plate is close to the target location, the gripper isn't touching
    # it, so pull the gripper out.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("near the target location")

# push-back: push the puck to the target location
def push_back(robot):
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
   