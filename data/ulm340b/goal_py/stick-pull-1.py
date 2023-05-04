
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Pull the stick towards the target location, to drag the thermos along
    # First, put the gripper above the stick, so that we can grab it without
    # pushing it around.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick", close_gripper=True)
    # Since the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with the stick"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # Now that we have the stick, drag the thermos to the target location.
    if check("the stick is below the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=True)

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Push the stick towards the target location, to push the thermos along
    # First, put the gripper above the stick, so that we can grab it without
    # pushing it around.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick", close_gripper=True)
    # Since the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the robot's gripper is vertically aligned with the stick"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # Now that we have the stick, push the thermos to the target location.
    if check("the stick is below the robot's gripper"):
        robot.move_gripper("near the target location", close_gripper=True)

# lever-pull: pull the lever with the robot's grip