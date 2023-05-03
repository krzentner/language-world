
    # Steps:
    #  1. Put gripper left of door lock
    #  2. Move hand above door lock
    #  3. Turn dial counterclockwise
    # We need a good vertical alignment with the door lock to get good control of
    # the dial, so we start by moving the gripper to the side of the door lock.
    if check("the robot's gripper is not to the left of the door lock and the robot's gripper is not in front the door lock"):
        robot.move("gripper to the left of the door lock")
    # Move the gripper up, lined up with the dial from above.
    if check("the robot's gripper is to the left of the door lock and the robot's gripper is not above the door lock"):
        robot.put("gripper above the door lock")
    # Now that the gripper is lined up, turn the dial counterclockwise.
    if check("the robot's gripper is above the door lock"):
        robot.turn("dial counterclockwise")