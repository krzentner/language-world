# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the plate back towards the target location
    #  3. Check if the plate is in the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is aligned with the plate but not near it, move the
    # gripper down to the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("the gripper into the plate")
    # If the gripper is near enough to the plate, we can slide it back.
    if check("the robot's gripper is near plate"):
        robot.slide("the plate back to the target location")
    # Check if the plate is in the target location.
    if check("the plate is in the target location"):
        robot.done()