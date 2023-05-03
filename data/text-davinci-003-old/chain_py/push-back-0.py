
    # Steps:
    #  1. Put gripper in front of the puck
    #  2. Push gripper into puck
    #  3. Slide the puck backwards to the target
    # The robot can try to slide the puck backwards by trapping it with the
    # gripper and moving the gripper back.
    # First, we need to get the gripper in front of the puck.
    if check("the robot's gripper is not in front of the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper in front of puck")
    # Once the gripper is in front of the puck, the gripper should be close
    # enough that the gripper can grab it.
    # The gripper needs to be open, otherwise we won't be able to move it.
    if check("the robot's gripper is in front of pudding and the robot's gripper is open"):
        robot.push("gripper into the puck")
    # Once we've trapped the puck, we can slide it back to the target location.
    if check("the robot's gripper and the puck are in front of the target location"):
        robot.slide("the puck to the goal")