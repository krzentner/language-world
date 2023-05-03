
    # Steps:
    #  1. Put gripper right of the plate handle
    #  2. Start pushing against the plate handle to slide the plate
    #  3. Push the plate harder
    # Before sliding the plate, we should put the robot's gripper some distance
    # from the plate handle.
    if check("the robot's gripper is not near the plate handle"):
        robot.move_gripper("near the plate handle")
    # Once the gripper is near the plate handle, start pushing against it with
    # the gripper.
    if check("the plate handle is right of the robot's gripper and the robot's gripper is not almost vertically aligned with the plate handle"):
        robot.move_gripper("almost vertically aligned with the plate handle", close_gripper=True)
    # If the gripper is almost vertically aligned with the plate handle, push
    # harder.
    if check("the robot's gripper is almost vertically aligned with the plate handle"):
        robot.move_gripper("right of the plate handle")

# turn-knob: turn the knob one complete turn
def turn_knob(robot):
    # Steps:
    #  1. Put gripper above the knob
    #  2. Grab the knob with the gripper
    #  3. Turn the knob clockwise
    #  4. Turn the knob back to the starting position
    # Begin by putting the gripper above the knob.
    if check("the robot's gripper is not vertically aligned with the knob"):
        robot.move_gripper("vertically aligned with the knob")
    # If the knob isn't around the gripper, put it around the knob.
    if check("the robot's gripper is not around knob and the robot's gripper is open"):
        robot.move_gripper("above the knob", close_gripper=True)
    # If the knob is around the gripper, turn it clockwise.
    if check("the robot's gripper is around knob and the knob is not in starting position"):
        robot.move_gripper("left of the knob")
    # If the knob has been turned, turn it back to its starting position.
    if check("the robot's gripper is left of the knob and the knob is not in starting position"):
        robot.move_gripper("insert around knob")