
    # Steps:
    #  1. Put gripper near plate
    #  2. Push the plate back and sideways
    #  3. Place the plate at the goal
    # If the gripper is not near the plate, move it to the side of the plate.
    # We don't need to be careful about the orientation, since we're going to
    # slide it to the target location.
    if check("the robot's gripper is not near the plate"):
        robot.grab("plate")
    # If the goal is behind the plate but to the left of the gripper, we can
    # start to slide the plate back and to the side.
    if check("the goal is behind plate and to the left of robot's gripper"):
        robot.push("plate back and to the side")
    # If the goal is behind the plate and to the right of the robot's gripper,
    # we can finish sliding it to the target location.
    if check("the goal is behind plate and to the right of robot's gripper"):
        robot.place("plate at goal")