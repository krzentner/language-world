
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper into button
    #  3. Slide button down
    # If the button is not below the gripper, move the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # Once the button is below the gripper, we should be able to push it down by
    # moving the gripper down towards the table.
    if check("the robot's gripper is above button"):
        robot.move_gripper("below the button")

# slider-turn-counterclockwise: turn the sliding button counterclockwise
def slider_turn_counterclockwise(robot):
    # Steps:
    #  1. Put gripper above slider knob
    #  2. Push gripper into slider knob
    #  3. Rotate the slider
    # First, put the gripper above the slider.
    if check("the robot's gripper is not vertically aligned with slider knob"):
        robot.move_gripper("vertically aligned with the slider knob")
    # Once the gripper is above the slider, push down into the slider.
    if check("the robot's gripper is vertically aligned with slider knob"):
        robot.move_gripper("right of the slider knob", close_gripper=True)
    # Once the gripper is in contact with the slider knob, keep pushing to the
    # right to rotate the slider.
    if check("the robot's gripper is right of the slider knob"):
        robot.move_gripper("vertically aligned with the slider knob", close_gripper=True)

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper almost above door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # We need to put the gripper almost above the door handle before we can grab
    # it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # If