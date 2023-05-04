
    # Steps:
    #  1. Move gripper to target location
    # Just move the gripper to the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")

# sweep: sweep the puck to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper roughly on the right side of the puck
    #  2. Move gripper into the puck to trap it
    #  3. Sweep the puck to the target location
    # The robot can slide the puck by trapping it by pushing from the side and
    # moving the gripper.
    # If the gripper is not to the right side of the puck, move it to the right
    # of the puck.
    if check("the robot's gripper is not near the puck and the robot's gripper is not to the right of the puck"):
        robot.move_gripper("near the puck")
    # If the puck is below the gripper as seen from the side, move the gripper
    # into the puck to slide it.
    if check("the robot's gripper is near the puck and the robot's gripper is not below the puck"):
        robot.move_gripper("below the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is below the puck"):
        robot.move_gripper("vertically aligned with the target location")

# toggle-switch-on: press the toggle switch up to turn it on
def toggle_switch_on(robot):
    # Steps:
    #  1. Line up gripper from front
    #  2. Close gripper on switch to turn on switch
    # If the gripper is not lined up from the front, line it up.
    if check("the robot's gripper is not forward aligned with toggle switch"):
        robot.move_gripper("above toggle switch", close_gripper=True)
    # If the gripper is lined up, press the toggle switch.
    if check("the robot's gripper