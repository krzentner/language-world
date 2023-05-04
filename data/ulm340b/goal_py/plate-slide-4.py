
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate into goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")

# switch-press: press the switch down
def switch_press(robot):
    # Steps:
    #  1. Put the gripper in front of the switch
    #  2. Move the gripper above the switch
    #  3. Push down on the switch
    # Move the gripper in front of the switch.
    if check("the robot's gripper is not forward aligned with switch"):
        robot.move_gripper("near the switch")
    # If the robot's gripper is not above the switch, move it above the switch.
    if check("the robot's gripper is above switch and the robot's gripper is in front of the switch"):
        robot.move_gripper("vertically aligned with the switch")
    # Now that the gripper is above the switch, move it down to push the switch.
    if check("the robot's gripper is forward aligned with the switch"):
        robot.move_gripper("above the switch