
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Reach to left of the thermos
    #  5. Push thermos to goal
    # First, put the gripper roughly above the stick, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # Once the gripper is above the stick and closed, it's probably holding the
    # stick.
    # Move the stick to the left of the thermos, so that it's ready to push the
    # thermos.
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.reach("stick to the left of the thermos")
    # Once the gripper is left of the thermos and above the thermos, use the
    # stick to push the thermos to the target location.
    # Make sure to close the gripper, so the stick doesn't fall out while we're
    # pushing.
    if check("the robot's gripper is to the left of the thermos and the robot's gripper is above the thermos"):
        robot.push("the thermos to the goal")

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Reach to right of the thermos
    #