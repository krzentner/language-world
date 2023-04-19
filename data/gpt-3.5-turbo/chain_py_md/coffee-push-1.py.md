# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target
    # Check if the gripper is above the mug
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above the mug")
    # If the gripper is not around the mug, put it around the mug
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around the mug")
    # Once the gripper is around the mug, we can move the mug to the target location
    if check("the robot's gripper is around the mug and the mug is below the robot's gripper"):
        robot.slide("the mug to the target")