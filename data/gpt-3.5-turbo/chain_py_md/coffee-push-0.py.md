# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    # 1. Put gripper above the coffee mug
    # 2. Grab the coffee mug with the gripper
    # 3. Move the coffee mug to the target location
    # First, put the gripper above the coffee mug.
    if check("the robot's gripper is not vertically aligned with the coffee mug"):
        robot.put("gripper above coffee mug")
    # If the gripper is not around the coffee mug, put it around the coffee mug
    if check("the robot's gripper is not around coffee mug and the robot's gripper is open"):
        robot.drop("gripper around coffee mug")
    # If the gripper is close and around the coffee mug, move the coffee mug to the target location
    if check("the robot's gripper is around coffee mug and the coffee mug is below the robot's gripper"):
        robot.slide("the coffee mug to the target location")