
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Put stick below the thermos
    #  5. Move stick below thermos
    # First, put the gripper roughly above stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe we
    # grabbed it.
    # Put the stick below the thermos.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above stick and the robot's gripper is closed"):
        robot.put("stick below thermos")
    # Move stick below thermos to push it towards the target.
    if check("the robot's gripper is near thermos"):
        robot.move("stick below thermos")

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Put stick above the thermos
    #  5. Move stick above thermos
    # First, put the gripper roughly above stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick