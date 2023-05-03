# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above coffee mug
    #  2. Grab the coffee mug with the gripper
    #  3. Move the coffee mug to the goal
    # First, put the gripper roughly above the coffee mug
    if check("the robot's gripper is not above the coffee mug"):
        robot.place("gripper above coffee mug")
    # If the gripper isn't around the coffee mug, put it around the coffee mug
    if check("the robot's gripper is not around the coffee mug and the robot's gripper is open"):
        robot.drop("gripper around coffee mug")
    # If the gripper is near the coffee mug and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near the coffee mug and the robot's gripper is open"):
        robot.close("gripper around coffee mug")
    # We closed the gripper, and the coffee mug is still near the gripper, so maybe we grabbed it.
    # Try to move the coffee mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above the coffee mug and the robot's gripper is closed"):
        robot.slide("the coffee mug to the goal")