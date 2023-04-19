
    # Steps:
    # 1. Put the hammer head over the top of the nail
    # 2. Swing the hammer towards the nail
    # 3. Pull the hammer back towards your body
    # First, the robot needs to put the hammer head above the head of the nail.
    if check("the robot's hammer head is not above the nail head"):
        robot.put("hammer head above the nail head")
    # Now that the robot has the hammer head just above the nail head, it can
    # swing the hammer towards the nail.
    if check("the robot's hammer head is above the nail head"):
        robot.swing("hammer back and forth")
    # Once the nail has been hit, we can pull the hammer back towards our body.
    if check("the hammer has hit the nail"):
        robot.pull("hammer back")