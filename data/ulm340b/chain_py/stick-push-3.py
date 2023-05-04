
    # Steps:
    #  1. Put gripper above stick
    #  2. Put gripper around stick
    #  3. Move stick to goal
    # First, put the gripper above stick, so that we don't bump the stick while
    # trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.put("gripper around stick")
    # Now, we should have grabbed the stick, so we can move it.
    if check("the robot's gripper is around stick"):
        robot.move("stick to goal")

# cloth-pull: grab the cloth and pull the thermos to the target location
def cloth_pull(robot):
    # Steps:
    #  1. Put gripper above cloth
    #  2. Drop gripper around cloth
    #  3. Close gripper around cloth
    #  4. Pull cloth to goal
    # First, put the gripper roughly above cloth, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cloth"):
        robot.put("gripper above cloth")
    # If the gripper isn't around the cloth, put it around the cloth.
    if check("the robot's gripper is not around cloth and the robot's gripper is open"):
        robot.drop("gripper around cloth")
    # If the gripper is near the cloth and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cloth and the robot's gripper is open"):
        robot.close("gripper around cloth")
    # We closed the gripper, and the cloth is still near the gripper, so maybe we
    # grabbed it.
    # Try to pull the cloth to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cloth and the robot's gripper