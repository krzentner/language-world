# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Put gripper near thermos
    #  4. Insert stick between thermos and the robot
    #  5. Push the thermos to the target location using the stick
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
    # Try to pick up the stick.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above stick and the robot's gripper is closed"):
        # Now that we have the stick, move it near the thermos we want to push.
        if check("the robot's gripper is not near thermos"):
            robot.move("gripper near the thermos")
        # Insert the stick between the thermos and the robot.
        if check("the stick is not between the robot and the thermos"):
            robot.insert("stick between the robot and the thermos")
        # Push the thermos to the target location using the stick.
        if check("the stick is between the robot and the thermos and the thermos is not at the target location"):
            robot.push("the thermos to the target location using the stick")