
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Push the lever up
    # First, put the gripper roughly above the lever handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not vertically aligned with the lever handle"):
        robot.move_gripper("vertically aligned with the lever handle")
    # Now that the gripper is lined up, try to grab the lever handle by closing
    # the gripper while moving it.
    # We also need to make sure that the robot's gripper is around the lever
    # handle.
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around the lever handle"):
        robot.move_gripper("around the lever handle")
    # If the gripper is around the lever handle, push it up to rotate the lever.
    if check("the robot's gripper is above the lever handle"):
        robot.move_gripper("above the lever handle")

# lever-push: rotate the lever down
def lever_push(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Push the lever down
    # First, put the gripper roughly above the lever handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not vertically aligned with the lever handle"):
        robot.move_gripper("vertically aligned with the lever handle")
    # Now that the gripper is lined up, try to grab the lever handle by closing
    # the gripper while moving it.
    # We also need to make sure that the robot's gripper is around the lever
    # handle.
    if check("the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around the lever handle"):
        robot.move_gripper("around the lever handle")
    # If the gripper is around the lever handle, push it down to rotate the
    # lever.
    if check("the robot's gripper is above the lever handle"):
        robot.