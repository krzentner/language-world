
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate, slide the plate to
    # the target location.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("above the target location")

# plate-pull: slide the plate into the target location
def plate_pull(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Pull the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate, pull the plate to
    # the target location.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("above the target location")

# box-pull: pull the box to the target location
def box_pull(robot):
    # Steps:
    #  1. Put gripper above the box
    #  2. Grab the box with the gripper
    #  3. Pull the box to the target location
    # First, put the gripper above the box.
    if check("the robot's gripper is not vertically aligned with the box"):
        robot.move_gripper("above the box", close_gripper=True)
    # As long the gripper is still mostly around the box, pull the box to the
    # target location.
    if check("the robot's gripper is above the box"):
        robot.move_gripper("above the target location")

# box-push: push the box to the target location
def box_push(robot):
    # Steps:
    #