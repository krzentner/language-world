
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door handle is
    # large and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door handle is aligned with the gripper as seen from in front, we
    # can push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("near the door handle")

# lever-pull: pull down on the lever to raise the platform
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around lever
    #  3. Pull lever down
    # We need to put the gripper above the lever before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.move_gripper("vertically aligned with the lever", close_gripper=True)
    # Once the gripper is lined up above the lever, we should be able to grab the
    # lever by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we can just pull the lever down.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("horizontally aligned with lever")

# reacher-reach: reach to the target location
def reacher_reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move_