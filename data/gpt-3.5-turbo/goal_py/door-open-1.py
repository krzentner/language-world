# Steps:
    #  1. Put gripper near the doorknob
    #  2. Grab the doorknob
    #  3. Pull the doorknob towards the robot
    # We need to put the gripper near the doorknob before we can grab it.
    if check("the robot's gripper is not near the doorknob"):
        robot.move_gripper("near the doorknob")
    # Once the gripper is near the doorknob, we should grab it by closing the
    # gripper around it.
    if check("the robot's gripper is near the doorknob and the robot's gripper is not around the doorknob"):
        robot.move_gripper("around the doorknob")
    # Once the gripper is around the doorknob, we just need to pull the doorknob
    # towards the robot to open the door.
    if check("the robot's gripper is around the doorknob"):
        robot.move_gripper("near the robot")