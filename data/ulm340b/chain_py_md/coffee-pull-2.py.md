

As long as you have a `# coffee-pull: grab the mug and pull it to the target location` as a comment and `def coffee_pull(robot)` your code will pass.

"""
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper near coffee handle
    #  2. Grab the coffee handle by closing the gripper around it
    #  3. Pull the coffee mug to the goal
    # If the gripper is not near the coffee handle, move it to be near the handle.
    # It doesn't need to be too precise, just near the coffee mug.
    if check("the robot's gripper is not near coffee handle"):
        robot.move("the gripper to be near the coffee handle")
    # If the gripper is not around the coffee handle, drop it down to grab the
    # coffee handle.
    # The robot's gripper doesn't need to be in any particular direction, just
    # around the coffee handle.
    if check("the robot's gripper is not around coffee handle and the robot's gripper is open"):
        robot.drop("the gripper around coffee handle")
    # Now that the coffee handle is lined up in the robot's gripper, just pull
    # the coffee mug to the goal.
    if check("the robot's gripper is around coffee handle and the coffee handle is not in the robot's gripper"):
        robot.pull("the coffee mug to the goal")


# Check if the robot's gripper is around the coffee handle or not.
def check_gripper_is_around_coffee_handle(robot):
    # If the robot's gripper is around the coffee handle, the robot has
    # grabbed the coffee handle.
    # So return True.
    if check("the robot's gripper is around coffee handle"):
        return True
    # Otherwise, return False.
    return False


# Check if the robot has successfully pulled the coffee mug.
def check_robot_has_pulled_coffee_mug(robot):
    # If the coffee handle is in the robot's gripper, the robot has pulled the
    # coffee mug.
    # So return True.
    if check("the robot's gripper is around coffee handle and the coffee handle