# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper back and to the side to slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, just grab it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.grab("plate")
    # Move the gripper back and to the side to slide the plate to the target location.
    if check("the robot's gripper is holding the plate"):
        robot.move("gripper back and to the side")
        robot.slide("the plate to the target location")