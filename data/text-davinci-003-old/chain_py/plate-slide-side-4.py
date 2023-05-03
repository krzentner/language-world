
    # Steps:
    #  1. Put gripper near the edge of the plate
    #  2. Push against the edge of the plate to slide it
    #  3. Push the plate harder to slide it faster
    # First, move the gripper near the edge of the plate.
    # Since the plate is larger than the gripper, check if the gripper is near
    # the plate instead of around it.
    if check("the gripper is not near the plate"):
        robot.move("gripper near edge of plate")
    # If the gripper is near the plate and the plate isn't at the goal yet, push
    # the plate away from the gripper.
    if check("the gripper is near the plate and the plate is not at the goal"):
        robot.push("plate away from gripper")
    # If the gripper is near the plate and the plate still isn't at the goal,
    # push harder and faster.
    if check("the gripper is near the plate and the plate is not at the goal"):
        robot.push("plate away from gripper harder and faster")