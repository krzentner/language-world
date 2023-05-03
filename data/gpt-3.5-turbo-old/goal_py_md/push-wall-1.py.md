# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal, even with the small wall in the way
    # The approach is similar to `push`, but now we have to make sure the gripper
    # doesn't collide with the small wall in between the puck and the target.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Check if the gripper and the puck are on the left, right or center of the
    # small wall.
    # If the gripper and puck are on the left side, push the puck towards the
    # right.
    if check("the robot's gripper and the puck are both left of the small wall"):
        robot.move_gripper("right of the puck")
    # If the gripper and puck are on the right side, push the puck towards the
    # left.
    elif check("the robot's gripper and the puck are both right of the small wall"):
        robot.move_gripper("left of the puck")
    # If the gripper and puck are on either side of the small wall, move the
    # gripper to the same side as the puck.
    else:
        if check("the robot's gripper is not aligned with the puck"):
            robot.move_gripper("left of the puck" if robot.gripper_x < robot.puck_x else "right of the puck")
    # Now that the gripper is aligned with the puck and the small wall, we can
    # slide the puck to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is aligned with the puck and the small wall"):
        robot.move_gripper("above the target location")