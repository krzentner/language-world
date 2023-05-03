# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Close gripper around hammer handle
    #  4. Lift hammer up
    #  5. Move gripper to the nail
    #  6. Bring hammer down to hit the nail
    #  7. Pull the hammer back up to its start position
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not above hammer handle"):
        robot.place("gripper above hammer handle")
    # If the gripper isn't around the hammer handle, put it around the handle.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    # If the gripper is near the hammer handle and open, close the gripper to grab the handle.
    if check("the robot's gripper is near hammer handle and the robot's gripper is open"):
        robot.close("gripper around hammer handle")
    # If the gripper is holding the hammer handle, lift it up out of its holder.
    if check("the robot's gripper is holding hammer handle"):
        robot.lift("hammer up")
    # Move the gripper to where the nail is.
    # There's no need to be too precise on the orientation.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.move("gripper above nail")
    # Bring the hammer down onto the nail.
    if check("the robot's gripper is vertically aligned with nail and hammer is not down"):
        robot.drop("hammer onto nail")
    # Pull the hammer back up to its starting position.
    if check("hammer is down and gripper is holding hammer handle"):
        robot.lift("hammer up")