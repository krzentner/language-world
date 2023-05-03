
    # Steps:
    #  1. Put gripper above basketball
    #  2. Drop gripper around basketball
    #  3. Close grippper around basketball
    #  4. Lift basketball upwards
    #  5. Align the basket to the hoop
    #  6. Move basketball over the hoop
    #  7. Release the basketball from the gripper
    # First, put the gripper above the basketball.
    if check("the robot's gripper is not above the basketball"):
        robot.plate("gripper above basketball")
    # If the gripper isn't around the basketball, put the gripper around it.
    if check("the robot's gripper is not around the basketball and the gripper is open"):
        robot.drop("gripper around basketball")
    # If the gripper is near the basketball, close the gripper around it so
    # that we can control the basketball without touching it with the floor.
    if check("the robot's gripper is near the basketball and the gripper is open"):
        robot.close("gripper around basketball")
    # Now that the basketball is in the gripper, we can lift it up.
    if check("the robot's gripper is closed and the basketball is above the floor"):
        robot.lift("basketball upwards")
    # Align the basketball to the hoop.
    if check("the robot's gripper is closed and the basketball is aligned with the hoop"):
        robot.align("basketball to hoop")
    # Move the basketball over the hoop.
    if check("the robot's gripper is closed and the basketball is over the hoop"):
        robot.move("basketball towards loop")
    # If the basketball is mostly in the hoop, release the gripper to drop it
    # into the hoop.
    if check("the basketball is in the hoop"):
        robot.release("gripper from basketball")