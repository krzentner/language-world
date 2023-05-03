# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to goal
    # The robot can move the mug by grabbing it and sliding it to the target location.
    # First, line up the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, grab the mug by closing the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so we must have grabbed it.
    # Now move the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.slide("the mug to the goal")