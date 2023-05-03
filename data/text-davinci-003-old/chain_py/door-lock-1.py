
    # Steps:
    #  1. Put gripper vertically above the lock
    #  2. Drop gripper to around the lock
    #  3. Turn the dial in the desired direction
    # We need to put the gripper above the lock before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door lock"):
        robot.place("gripper above door lock")
    # Once the gripper is lined up above the lock, we should be able to grab the
    # lock by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door lock and the robot's gripper is not around door lock"):
        robot.drop("gripper around door lock")
    # Now that the gripper is mostly around the lock, try turning the dial in
    # the appropriate direction.
    if check("the robot's gripper is around the door lock"):
        robot.turn("dial to the desired direction")