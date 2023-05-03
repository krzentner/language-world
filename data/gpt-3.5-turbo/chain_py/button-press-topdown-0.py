# Steps
    # 1. Put gripper above the button
    # 2. Slide the gripper down onto the button
    # 3. Push the button down
    # First, we should put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # Once the gripper is above the button, we can slide it down onto the button.
    if check("the robot's gripper is above the button and not touching it"):
        robot.slide("gripper onto button")
    # Once the gripper is on the button, we can push it down.
    if check("the robot's gripper is on the button"):
        robot.push("button down")