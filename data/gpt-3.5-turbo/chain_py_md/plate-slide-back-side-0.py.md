# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Lift the plate from the surface
    #  4. Go back along the same path that the gripper came from
    #  5. Lower the plate until it touches the surface again
    #  6. Move the plate to the target location by sliding it sideways
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, grab the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Once the gripper has grabbed the plate, lift it from the surface.
    if check("the robot's gripper is around plate"):
        robot.lift("plate")
    # Move the gripper back along the same path that it came from until it
    # reaches its starting position.
    if check("the robot's gripper is holding the plate and the gripper isn't at the starting position"):
        # TODO: move the gripper back along the same path the plate slid from
        pass
    # Lower the plate until it touches the surface again.
    if check("the robot's gripper is holding the plate and the plate is not touching the surface"):
        robot.put("gripper above initial plate position")
        robot.put("plate on surface")
    # Once the plate is on the surface, move it to the target location by sliding
    # it sideways.
    if check("the plate is touching the surface"):
        robot.slide("plate to target location")