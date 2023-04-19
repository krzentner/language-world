# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Put the end of the stick into the thermos handle
    #  5. Push the stick to make it into the thermos handle
    #  6. Lift the stick with the thermos handle and slide the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it.
    # Try to use the stick to push down and hook the thermos handle.
    # If we didn't grab the thermos, we'll just go back to an earlier step.
    if check("the stick is in the correct position in the thermos handle"):
        robot.lift("stick with thermos handle")
        robot.slide("thermos to the goal")