
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate back
    # We won't actually grab the plate, but grab it by putting it below the
    # gripper as seen from above.
    # If the plate isn't below the gripper, put the gripper above the plate.
    if check("the plate is not below the robot's gripper"):
        robot.put("gripper above plate")
    # As long as the gripper is still above the plate, let's move the gripper
    # around and align it under the plate.
    # As long as the gripper is still above the plate, just keep pushing down
    # until it's under the plate.
    if check("the robot's gripper is above plate"):
        robot.push("gripper down")
    # If the gripper is under the plate, just keep pushing it back.
    if check("the robot's gripper is below plate"):
        robot.slide("plate back")