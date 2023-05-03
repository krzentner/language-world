
    # Steps:
    #  1. Put gripper over target
    #  2. Move gripper to the target
    # Start by placing the gripper roughly over the target location.
    # This makes sure the target is in view of the robot's camera.
    if check("the robot's gripper is not above the target"):
        robot.put("gripper above target")
    # When the gripper is over the target, just start moving towards the target.
    if check("the robot's gripper is above the target and the robot's gripper is not at the target"):
        robot.move("gripper to target")