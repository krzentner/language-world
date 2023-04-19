# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    # 1. Put gripper around door
    # 2. Push the door closed to the target location
    # First, put the gripper around the door.
    if check("the robot's gripper is not around the door and the robot's gripper is open"):
        robot.drop("gripper around door")
    # If the gripper is around the door, push the door closed to the target location.
    if check("the robot's gripper is around the door"):
        robot.push("door closed to target location")