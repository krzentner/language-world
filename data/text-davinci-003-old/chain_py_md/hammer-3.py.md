

# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer
    #  2. Grab hammer with gripper
    #  3. Put gripper above nail
    #  4. Push hammer downward onto nail 
    # First, put the gripper above the hammer to grab it.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # Now that the gripper is above the hammer, close the gripper
    # to grab the hammer.
    if check("the robot's gripper is above the hammer and the robot's gripper is open"):
        robot.close("around hammer")
    # Once we have the hammer, put the gripper above the nail.
    if check("the robot's gripper is holding the hammer and the robot's gripper is not above nail"):
        robot.put("gripper above nail")
    # Finally, we can use the hammer to hit the nail.
    if check("the robot's gripper is above the nail"):
        robot.push("hammer downward onto nail")