
    # Steps:
    #  1. Orient gripper so that it is horizontally aligned with the best place to grab the stick
    #  2. Grasp the stick
    #  3. Put the stick underneath the thermos
    #  4. Push the thermos to the goal
    # First, the robot needs to orient its gripper so that it is horizontally
    # aligned with the best place to grab the stick.
    if check("the robot's gripper is not horizontally aligned with the best place to grab the stick"):
        robot.orient("gripper to the stick")
    # Once the gripper is aligned with the stick, try to grab it.
    if check("the robot's gripper is horizontally aligned with the best place to grab the stick"):
        robot.grasp("the stick")
    # If the robot has a stick in its gripper, put it underneath the thermos.
    if check("the robot has the stick in its gripper"):
        robot.put("stick underneath thermos")
    # Now that the stick is underneath the thermos, try pushing the thermos to
    # the goal.
    if check("the stick is underneath the thermos"):
        robot.push("thermos to goal")