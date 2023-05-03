
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Push puck against wall
    #  4. Slide puck to goal
    # As with push, we should put the gripper above the puck first.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # As with push, align the gripper with the puck by trapping it from above.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # Once the puck is below the gripper again, push it against the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.push("the puck against the wall")
    # Last, slide the puck to the goal.
    if check("the puck is against the wall and the wall is between the puck and the target"):
        robot.slide("the puck to the goal")