# hammer: hit the nail with the hammer.
# def hammer(robot):
    # Steps:
    # 1. Put the gripper above the hammer handle.
    # 2. Close the gripper around the handle.
    # 3. Move the hammer to above the nail.
    # 4. Move the hammer down to hit the nail.
    # 5. Lift the hammer back up.
    # 6. Open the gripper to release the handle.
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not vertically aligned with the hammer handle"):
        robot.move("the gripper above the hammer handle")
    # We grab the handle when the gripper is above it.
    if check("the robot's gripper is above the hammer handle and the robot's gripper is open"):
        robot.grab("hammer handle")
    # Move the hammer to above the nail.
    if check("the hammer is not above the nail"):
        robot.move("the hammer above the nail")
    # Move the hammer down to hit the nail and then lift it back up.
    if check("the hammer is above the nail and the hammer is not touching the nail"):
        robot.push("hammer down onto the nail")
        robot.pull("hammer up")
    # Release the handle by opening the gripper.
    if check("the hammer has hit the nail and the robot's gripper is closed"):
        robot.open("gripper to release hammer handle")