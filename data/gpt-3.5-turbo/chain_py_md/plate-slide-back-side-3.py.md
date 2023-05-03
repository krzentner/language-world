# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper next to plate
    #  2. Grab plate with gripper
    #  3. Move gripper and plate back to target location
    # First, move the gripper next to the plate.
    if check("the robot's gripper is not near the plate and to the side of it"):
        robot.move("gripper next to plate")
    # Once the gripper is next to the plate, grab it.
    if check("the gripper is near the plate and the robot's gripper is not around the plate"):
        robot.grab("plate")
    # If the plate is gripped, move the gripper and plate back to the target location.
    if check("the gripper is around the plate"):
        robot.move("gripper and plate back to target location")