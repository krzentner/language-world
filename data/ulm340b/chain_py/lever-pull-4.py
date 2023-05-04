
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab lever
    #  3. Pull lever up
    # First, put the gripper above the lever, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # If the gripper is above the lever, try to grab it.
    if check("the robot's gripper is above the lever and the robot's gripper is not near the lever"):
        robot.move("gripper to the lever")
    # Once the gripper is around the lever, we can just pull the lever up.
    if check("the robot's gripper is near the lever"):
        robot.pull("lever up")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Move gripper down to door handle
    #  3. Close the door
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.drop("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being closed, so keep pushing.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door closed")

# lever-push: rotate the lever down
def lever_push(robot):
    # Steps:
    #  1. Put gripper below the lever
    #  2. Grab lever
    #  3. Push lever down
    # First, put the gripper below the lever, so that we don't