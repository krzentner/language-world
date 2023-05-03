# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put the gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the gripper to the target location
    #  4. Push the mug towards the target
    # First, put the gripper above the mug so that we don't knock it over while
    # trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # Once the gripper is roughly above the mug, we can try to grab it.
    if check("the robot's gripper is above the mug and the robot's gripper is open"):
        robot.grab("mug")
    # If the gripper is around the mug, we may have grabbed it.
    # Move the gripper to the target location.
    if check("the robot's gripper is around the mug"):
        robot.place("gripper at target")
    # If the gripper is at the target location, slide the mug towards the target.
    if check("the robot's gripper is at target"):
        robot.slide("mug to goal")