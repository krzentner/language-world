

Steps:
1. Put the gripper above the dial of the door
2. Lower the gripper to the dial
3. Turn the dial 

    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Once the gripper is lined up above the dial, drop it down to grab it.
    if check("the robot's gripper is above the dial"):
        robot.move_gripper("around the dial")
    # Rotate the dial to the desired direction/visual cue.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("horizontally aligned with the dial")