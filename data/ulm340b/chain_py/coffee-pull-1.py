
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull the mug to the goal location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to pull the mug to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near the mug and the robot's gripper is closed"):
        robot.pull("coffee to goal")

# spatula-slide: grab the spatula and slide it to the target location
def spatula_slide(robot):
    # Steps:
    #  1. Put gripper above spatula
    #  2. Drop gripper around spatula
    #  3. Close gripper around spatula
    #  4. Slide spatula towards the goal location
    # First, put the gripper above the spatula.
    if check("the robot's gripper is not above the spatula"):
        robot.place("gripper above spatula")
    # If the gripper isn't around the spatula, put it around the spatula.
    if check("the robot's gripper is not around spatula and the robot's gripper is open"):
        robot.drop("gripper around spatula")
    # If the gripper is near the spatula and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near spatula and the robot's