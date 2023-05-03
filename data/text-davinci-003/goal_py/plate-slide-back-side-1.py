
    # Steps:
    #  1. Put gripper above plate handle
    #  2. Drop gripper around plate handle
    #  3. Pull plate towards robot
    #  4. Rotate plate sideways
    #  5. Move plate to goal
    # We want to grab the plate by the handle, so put the gripper above the
    # handle.
    if check("the robot's gripper is not vertically aligned with the plate handle"):
        robot.move_gripper("vertically aligned with the plate handle")
    # Once the gripper is above the handle, drop the gripper around the handle.
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not around plate handle"):
        robot.move_gripper("around the plate handle")
    # Now that the plate is grabbed by the handle, just pull the plate towards the
    # robot to rotate the plate.
    if check("the robot's gripper is around plate handle"):
        robot.move_gripper("left of the plate handle")

# plate-slide-forward-side: slide the plate forwards sideways into the target location
def plate_slide_forward_side(robot):
    # Steps:
    #  1. Put gripper above plate handle
    #  2. Drop gripper around plate handle
    #  3. Push plate away from robot
    #  4. Rotate plate and slide sideways
    #  5. Move plate to goal
    # First, put the gripper above the plate handle.
    if check("the robot's gripper is not vertically aligned with the plate handle"):
        robot.move_gripper("vertically aligned with the plate handle")
    # Once the gripper is above the handle, drop the gripper around the handle.
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not around plate handle"):
        robot.move_gripper("around the plate handle")
    # Now that the plate is grabbed by the handle, just push the plate away from
    # the robot to rotate the plate.
    if check("the robot's gripper is around plate handle"):
        robot.move_gripper("right of the plate handle")