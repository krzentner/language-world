# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper near the lever knob
    #  2. Grab the lever knob with the gripper
    #  3. Rotate the gripper until the lever is pulled up
    # Move the gripper near the lever knob.
    if check("the robot's gripper is not near the lever knob"):
        robot.move_gripper("near the lever knob")
    # If the gripper is lined up with the lever knob, grab it.
    if check("the robot's gripper is close to the lever knob and the robot's gripper is open"):
        robot.move_gripper("around the lever knob", close_gripper=True)
    # Once the gripper is around the lever knob, rotate the gripper until the lever is pulled up.
    if check("the lever is not pulled up"):
        robot.rotate_gripper("lever_up")