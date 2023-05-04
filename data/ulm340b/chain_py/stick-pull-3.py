
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to goal
    #  5. Close thermos into stick
    # First, put the gripper roughly above the stick, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the stick and the robot's gripper is open"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    # We closed the gripper, and the stick is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the stick to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above stick and the robot's gripper is closed and the robot's gripper is forward aligned with stick"):
        robot.move("stick to goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to goal
    #  5. Close thermos into stick
    # First, put the gripper roughly above the stick, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the stick and the robot's gripper is open"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it