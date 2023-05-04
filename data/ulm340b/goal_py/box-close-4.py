
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Drop gripper around the box lid
    #  3. Close gripper around the box lid
    #  4. Slide box lid over the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the robot's gripper is not around the box lid, put it around the box
    # lid.
    if check("the robot's gripper is not around the box lid"):
        robot.move_gripper("above the box lid", close_gripper=True)
    # If the gripper is near the box lid, maybe we can grab the box lid by
    # closing the gripper.
    if check("the robot's gripper is around the box lid and the robot's gripper is open"):
        robot.move_gripper("above the box lid")
    # Once the box lid is in the gripper, we just slide it onto the box.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box")

# push-lever: turn the lever to the target location
def push_lever(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Rotate lever to target location
    # First, put the gripper above the lever.
    if check("the robot's gripper is not above lever"):
        robot.move_gripper("above lever")
    # If the robot's gripper is not around lever, put it around lever.
    if check("the robot's gripper is not around lever"):
        robot.move_gripper("near lever", close_gripper=True)
    # Once the gripper is around the lever, turn the lever to the target
    # location.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("above lever")

# peg-unstack: put one of the pucks on the table
def peg_unstack(robot):
    # Steps:
    # 