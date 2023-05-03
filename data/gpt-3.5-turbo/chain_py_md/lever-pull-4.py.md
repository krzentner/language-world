# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper below the lever
    #  2. Grab the lever with gripper
    #  3. Rotate the gripper up to turn the lever
    # First, put the gripper below the lever.
    if check("the robot's gripper is not below the lever"):
        robot.put("gripper below lever")
    # If the gripper is not around the lever, grab it.
    if check("the robot's gripper is not around the lever and the gripper is open"):
        robot.drop("gripper around lever")
    # If the gripper is around the lever and the lever is not horizontal, keep rotating the gripper up.
    if check("the robot's gripper is around the lever and the lever is not horizontal"):
        robot.rotate("gripper up to turn lever")