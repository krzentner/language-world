# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    # 1. Put gripper right above the lever
    # 2. Grab the lever
    # 3. Rotate the lever up
    # First, check if the gripper is above the lever. If not, move the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    # Once the gripper is above the lever, grab it.
    if check("the robot's gripper is vertically aligned with the lever and the gripper is not around the lever"):
        robot.grab("lever")
    # Now we have the lever in the gripper, and it's roughly lined up with the target position.
    # Rotate the lever up to the target position.
    if check("the robot's gripper is around the lever"):
        robot.rotate("lever up")