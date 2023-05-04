
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate into the target location
    # If the gripper is not above the plate, move the gripper above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not near plate"):
        robot.put("the gripper above the plate")
    # If the gripper is above the plate and not around it, put the gripper
    # around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is above plate"):
        robot.drop("the gripper around the plate")
    # If the gripper is around the plate, slide the plate back to the goal.
    if check("the robot's gripper is around plate"):
        robot.slide("the plate back to the goal")

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Move gripper forward to grab plate
    #  3. Slide the plate into the target location
    # If the gripper is not above the plate, move the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.put("the gripper above the plate")
    # If the gripper is above the plate, move the gripper forward to grab the
    # plate.
    if check("the robot's gripper is above plate and the robot's gripper is not near plate"):
        robot.reach("the gripper forward towards plate")
    # If the gripper is near the plate, slide the plate back to the goal.
    if check("the robot's gripper is near plate"):
        robot.slide("the plate back to the goal")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate into the target location
    # If the gripper is not above the plate,