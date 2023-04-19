# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Align the gripper with the handle
    #  2. Close the gripper around the handle
    #  3. Pull up the handle
    
    # First, align the gripper with the handle by moving it to a position above it
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, grab it by closing the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # Now that the gripper is around the handle, pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")