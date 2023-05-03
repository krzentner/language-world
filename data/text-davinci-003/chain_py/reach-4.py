
    # Steps:
    #  1. Reach out arm
    #  2. Move arm towards target
    #  3. Move arm past target
    #  4. Put gripper around the target
    # After the robot moves the arm, it's in a position to reach with the
    # gripper.
    robot.reach("out arm")
    # Move the arm towards the target location.
    robot.move("towards target")
    # Make sure the arm goes slightly past the target location, then circle
    # back for the gripper.
    robot.move("past target")
    # Once the arm is in a good position, the gripper can grab the target.
    robot.put("gripper around the target")