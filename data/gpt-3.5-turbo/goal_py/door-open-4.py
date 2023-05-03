# Steps:
    # 1. Move the gripper to the doorknob
    # 2. Wrap the gripper around the doorknob
    # 3. Pull the gripper towards the robot to open the door
    # We first need to position the gripper around the doorknob. If it is not already near the doorknob, we can move it there.
    if check("the robot's gripper is not near the doorknob"):
        robot.move_gripper("near the doorknob", close_gripper=True)
    # Once the gripper is near the doorknob we can wrap it around and pull towards the robot to open the door
    if check("the robot's gripper is near the doorknob and the gripper is not wrapped around the doorknob"):
        robot.move_gripper("around the doorknob", close_gripper=True)
    if check("the gripper is wrapped around the doorknob and is not pulled towards the robot"):
        robot.move_gripper("towards the robot")