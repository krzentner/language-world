# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    # 1. Put gripper above the handle of the door
    # 2. Grab the handle with the gripper
    # 3. Push the door closed
    # First, move the gripper above the handle of the door.
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the handle, grab the handle by moving
    # the gripper to the right around it.
    if check("the robot's gripper is above the door handle and the robot's gripper is not around the door handle"):
        robot.move("gripper around door handle to the right")
    # Once the gripper is around the handle, we can push the door closed by
    # moving the gripper to the right while keeping it mostly around the handle.
    if check("the robot's gripper is around the door handle"):
        robot.push("door closed")