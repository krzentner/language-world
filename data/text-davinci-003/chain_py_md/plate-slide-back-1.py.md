

The `plate-slide-back` task requires the robot to slide a plate back into the target location.

# Steps:
#  1. Put gripper above plate
#  2. Push plate back into target location

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper is almost overhead of the plate, we should be able to slide
    # the plate back to the target.
    if check("the robot's gripper is almost overhead of the plate"):
        robot.push("plate back to target")