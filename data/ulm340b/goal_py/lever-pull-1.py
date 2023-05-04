
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull the lever upwards
    # First, put the gripper mostly above lever.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.move_gripper("vertically aligned with the lever")
    # As long as the gripper is lined up, we should be able to grab the lever by
    # closing the gripper.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # If we've grabbed the lever, we can move it upwards by moving the gripper
    # above the lever.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("above the lever")

# lever-push: push the lever down
def lever_push(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Push lever downwards
    # First, put the gripper above lever.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.move_gripper("vertically aligned with the lever", close_gripper=True)
    # If the gripper is lined up and the gripper is open, we can grab the lever
    # by closing the gripper.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # If we've grabbed the lever, we can move it downwards by moving the gripper
    # below the lever.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("below the lever")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # First, put the grip