
    # Steps:
    #  1. Put gripper above door
    #  2. Push the door closed
    # We need to put the gripper above the door before we can push it closed,
    # because of the angle of the robot's gripper and the door.
    if check("the robot's gripper is not above the door"):
        robot.put("gripper above door")
    # As long as the gripper is above the door, we can try to push the door
    # closed.
    if check("the robot's gripper is above the door"):
        robot.push("door closed")