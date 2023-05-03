# Steps:
    # 1. Put gripper against the door
    # 2. Push the door closed
    # If the gripper isn't against the door, move it there.
    if check("the robot's gripper is not against the door"):
        robot.move("gripper against the door")
    # If the robot's gripper is against the door, push it closed towards the
    # target location.
    if check("the robot's gripper is against the door"):
        robot.push("door closed")