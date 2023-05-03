# Steps:
    #  1. Put gripper above door knob
    #  2. Drop gripper around door knob
    #  3. Turn door knob to open door
    # We need to put the gripper roughly above the door knob first, so that we
    # can grab it without knocking it with the gripper.
    if check("the robot's gripper is not above the door knob"):
        robot.put("gripper above door knob")
    # Once the gripper is above the door knob, we can grab it by dropping the
    # gripper around it.
    if check("the robot's gripper is above the door knob and the robot's gripper is not around the door knob"):
        robot.drop("gripper around door knob")
    # Now that the gripper is around the door knob, we can turn it to open the
    # door.
    if check("the robot's gripper is around the door knob"):
        robot.turn("door knob to open door")