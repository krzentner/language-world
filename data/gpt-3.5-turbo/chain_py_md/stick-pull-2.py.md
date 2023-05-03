# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to the thermos
    #  5. Grab the stick with two hands
    #  6. Move one of the grippers closer to the target location
    #  7. Move the other gripper to the far end of the stick
    #  8. Pull both grippers towards the target location
    #  9. Release the stick
    #  10. Move the gripper back to the initial position
    # First, put the gripper roughly above the stick, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we grabbed it.
    # Try to move the stick to the thermos.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above stick and the robot's gripper is closed"):
        robot.place("stick at thermos")
        # Now that the stick is near the thermos, grab the stick with the other gripper.
        if check("one of the grippers is not around stick and the robot's grippers are open"):
            robot.grab("stick")
        # Move the second gripper to the other end of the stick.
        if check("both grippers are around stick and one gripper is not at the end of the stick"):
            robot.move("second gripper to end of stick")
        # Once both grippers are on the stick and at the right positions, pull them towards the target location.
        if check("both grippers are on stick and lined up with the target location"):
            robot.pull("grippers toward target")
            # Release the stick.
            robot.drop("grippers release stick")
            # Finally, move the gripper back to the initial position.
            robot.move("grippers to initial position")