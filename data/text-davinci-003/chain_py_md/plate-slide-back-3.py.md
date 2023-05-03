

The task is to slide a plate back into the target location.

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper in between plate and surface
    #  3. Slide plate back to target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate isn't forward of the gripper, push the gripper so that it's
    # in between the plate and the surface.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.push("gripper in between plate and surface")
    # Once the gripper is in between the plate and the surface, slide the plate
    # back to the target location.
    if check("the robot's gripper is in between the plate and surface"):
        robot.slide("plate back to target location")