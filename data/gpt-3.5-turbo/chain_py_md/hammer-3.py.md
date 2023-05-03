# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer handle
    #  2. Grab the hammer with the gripper
    #  3. Put the gripper near the nail
    #  4. Swing the hammer down to hit the nail
    # First, line up the gripper above the hammer handle.
    if check("the gripper is not above the hammer handle"):
        robot.put("gripper above hammer handle")
    # Once the gripper is lined up, grab the hammer with the gripper.
    if check("the gripper is above the hammer handle and the gripper is open"):
        robot.grab("hammer handle")
    # Bring the gripper near the nail by moving the robot (the nail should be
    # near the hammer).
    if check("the gripper is around the hammer handle"):
        robot.reach("to nail")
    # Swing the hammer down to hit the nail.
    if check("the gripper is near the nail"):
        robot.swing("hammer down on nail")