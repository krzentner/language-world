# door-open: pull the door open
def door_open(robot):
    # Steps:
    # 1. Put the gripper on the door knob
    # 2. Turn the door knob to open the door
    # First, we need to put the gripper on the door knob. If the gripper is not above the door knob,
    # we need to move it there.
    if check("the robot's gripper is not above the door knob"):
        robot.move_gripper("above the door knob")
    # Once the gripper is above the door knob, we need to rotate it to open the door. We can do this by
    # turning the gripper to the left or right. The direction doesn't matter as long as the door opens.
    if check("the robot's gripper is above the door knob"):
        robot.move_gripper("around the door knob")