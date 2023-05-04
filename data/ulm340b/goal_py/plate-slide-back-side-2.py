
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the goal
    #  4. Slide the plate sideways into the goal
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate becomes right of the gripper, go back to putting the gripper
    # above the plate.
    if check("plate is not right of the robot's gripper"):
        robot.move_gripper("left of the plate")
    # Because the plate is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target location, line up the plate with the target
    # location.
    if check("plate is vertically aligned with the goal"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is lined up with the target location to the side, slide it
    # in.
    if check("the plate is not vertically aligned with the goal and the plate is forward aligned with the robot's gripper"):
        robot.move_gripper("horizontally aligned with the goal")

# plate-slide-forward-side: slide the plate forward sideways into the target location
def plate_slide_forward_side(robot):
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the goal
    #  4. Slide the plate sideways into the goal
    # First, put the gripper in front of the plate.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.move_gripper("horizontally aligned with the plate")
    # If the plate becomes left of the gripper, go back to