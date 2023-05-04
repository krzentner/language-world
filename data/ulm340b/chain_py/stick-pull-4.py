
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Pull thermos with stick
    # First, put the gripper above the stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick"):
        robot.drop("gripper around stick")
    # If the gripper is above and around the stick, then maybe we have it.
    # Try to pull the thermos with the stick.
    # If we didn't grab the stick, we'll go back to an earlier step.
    if check("the robot's gripper is around stick and the robot's gripper is above stick"):
        robot.drag("stick to the thermos to the goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Push thermos with stick
    # First, put the gripper above the stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick"):
        robot.drop("gripper around stick")
    # If the gripper is above and around the stick, then maybe we have it.
    # Try to push the thermos with the stick.
    # If we didn't grab the stick, we'll go back to an earlier step.
    if check("the robot's gripper is around stick and the robot's gripper is above stick"):
        robot.push("stick into thermos towards the goal")

# stick-sweep: move the stick from the middle of the table to the target location
def stick_sweep(robot):
  