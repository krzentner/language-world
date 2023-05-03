# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with the gripper
    #  3. Push plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a large object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long as the gripper is still mostly around the plate and the plate isn't lined
    # up with the target location, slide the plate back towards the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("almost horizontally aligned with the plate")
    # Once the plate is almost horizontally aligned with the target location, keep pushing it back
    if check("the plate is horizontally aligned with the target location and the robot's gripper is sliding the plate towards the target location"):
        robot.move_gripper("almost vertically aligned with the target location")