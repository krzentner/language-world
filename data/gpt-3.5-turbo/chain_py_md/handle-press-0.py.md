# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    # 1. Put gripper near handle
    # 2. Drop gripper around handle
    # 3. Push down on handle
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    # Once the gripper is near the handle, drop it around the handle.
    if check("the robot's gripper is not around the handle" and "the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, we can push down on it.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")