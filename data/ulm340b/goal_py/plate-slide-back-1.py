
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Slide plate into target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate")
    # Now, drop the gripper around the plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("around plate")
    # The plate should now be below the gripper.
    # Push it towards the target location.
    if check("the plate is below the robot's gripper"):
        robot.move_gripper("above plate")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around plate
    #  3. Slide plate into target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Now, drop the gripper around the plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("around the plate")
    # The plate should now be below the gripper.
    # Push it towards the target location.
    if check("the plate is below the robot's gripper"):
        robot.move_gripper("horizontally aligned with the plate")

# plate-stack: put the plate on top of the target location
def plate_stack(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around plate
    #  3. Lift plate above target location
    #  4. Drop plate onto target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Now, drop the gripper around the plate.
    if check("the