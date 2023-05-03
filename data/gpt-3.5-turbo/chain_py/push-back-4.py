# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck towards the robot
    #  4. Push gripper into top of puck
    #  5. Slide puck to goal
    # We start by putting the gripper above the puck.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # Then we push the gripper into the bottom of the puck to start sliding it
    # back towards the robot.
    if check("the robot's gripper is above the puck and not pushing into it"):
        robot.push("the gripper into the bottom of the puck")
    # Once the puck is back towards the robot, we push the gripper back into the
    # top of the puck.
    if check("the puck is back towards the robot and the gripper is pushing into the bottom of the puck"):
        robot.push("the gripper into the top of the puck")
    # Finally, we can slide the puck towards the goal, with the gripper
    # maintaining control.
    if check("the gripper is pushing into the top of the puck and the puck is aligned with the goal"):
        robot.slide("the puck to the goal")