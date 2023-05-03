# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper on the lever handle
    #  2. Tilt the gripper vertically to hook onto the lever handle
    #  3. Pull the lever upwards
    # Put the gripper on the lever handle.
    if check("the robot's gripper is not on the lever handle"):
        robot.move_gripper("on the lever handle")
    # Tilt the gripper vertically to hook onto the lever handle.
    if check("the robot's gripper is on the lever handle and the robot's gripper is not vertically tilted"):
        robot.move_gripper("tilted vertically", close_gripper=True)
    # Pull the lever upwards.
    if check("the robot's gripper is vertically tilted"):
        robot.move_gripper("tilted vertically and pulled upwards")