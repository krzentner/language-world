
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Slide the mug to goal
    # First, put the gripper above the mug, so that we don't knock it over while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with mug"):
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
    # Try to slide the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.slide("mug to goal")

# coffee-pour: pour the mug from the starting position to the target position
def coffee_pour(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Lift mug up
    #  5. Move mug to goal
    #  6. Pour mug
    # First, put the gripper above the mug, so that we don't knock it over while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.place("gripper above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
       