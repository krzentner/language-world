
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Slide the plate in
    #  3. Push the plate in
    # If the plate is behind the robot's gripper, it needs to be in front of it.
    if check("the plate is behind the robot's gripper and the robot's gripper is not in front of plate"):
        robot.put("gripper in front of plate")
    # Once the gripper is in front of the plate, the plate should start sliding
    # in. If it doesn't, we'll push it.
    if check("the robot's gripper is in front of plate but the plate is not going in yet"):
        robot.slide("plate in")
    # The plate might need some extra push.
    if check("the robot's gripper is in front of plate but the plate is not fully in yet"):
        robot.push("plate in")