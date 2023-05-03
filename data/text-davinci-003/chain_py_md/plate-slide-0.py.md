
    
    
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into the plate, trapping it
    #  3. Slide the plate to the goal location
    # First, the gripper should be put above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper is aligned with the plate but not near it, move the gripper 
    # down to trap the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # If the gripper is near the plate, we've probably trapped the plate and can 
    # slide it to the goal. Close the gripper to make sure we keep control of it.
    if check("the robot's gripper is near the plate and the gripper is open"):
        robot.close("gripper around plate")
    # Slide the plate to the goal.
    if check("the robot's gripper is closed around the plate"):
        robot.slide("plate to goal")