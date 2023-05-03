
    # Steps:
    #  1. Put robot's gripper above the hammer 
    #  2. Grasp the hammer
    #  3. Place the head of the hammer above the nail 
    #  4. Push the hammer against the nail
    #  5. Lift the hammer again
    # Move the robot's gripper to above the hammer to get ready to grab it
    if check("the robot's gripper is not above hammer"):
        robot.put("gripper above hammer")
    # If the hammer is in line with the gripper, grab it.
    if check("the robot's gripper is forward aligned with the hammer and the robot's gripper is not around hammer"):
        robot.grab("hammer")
    # If the gripper is lined up above the nail, bring the hammer head down
    # against it.
    if check("the robot's gripper is above nail and the robot's gripper is forward aligned with the nail"):
        robot.place("hammer head above nail")
    # As long as the gripper is still rotated above the nail and the hammer is
    # still up above the nail, keep pushing against the nail with the hammer.
    if check("the robot's gripper is above nail and the robot's gripper is forward aligned with the nail and the hammer is up above the nail"):
        robot.push("hammer against nail")
    # Now that the nail is hammered in, it's time to lift the hammer back up.
    # The hammer is still in the gripper and the gripper is rotated above the
    # nail, so just lift the hammer back up.
    if check("the robot's gripper is above nail and the robot's gripper is forward aligned with the nail and the hammer is down against the nail"):
        robot.lift("hammer up")